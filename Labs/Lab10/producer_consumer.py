import concurrent.futures
import logging
import time
import threading
import datetime

from Labs.Lab10.city_processor import CityOverheadTimes, ISSDataRequest, City, CityDatabase


class CityOverheadTimeQueue:
    """
    CityOverheadTimeQueue class.
    """
    def __init__(self):
        """
        Initialize CityOverheadTimeQueue class.
        """
        self.data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: CityOverheadTimes) -> None:
        """
        Add CityOverheadTimes object to the queue.
        :param overhead_time: CityOverheadTimes object
        """
        with self.access_queue_lock:
            self.data_queue.append(overhead_time)

    def get(self) -> CityOverheadTimes:
        """
        Get an object from the queue and remove it.
        :return: CityOverheadTimes object
        """
        with self.access_queue_lock:
            queue = self.data_queue[0]
            del(self.data_queue[0])
        return queue

    def __len__(self) -> int:
        """
        Get length of the data_queue
        :return: integer
        """
        return len(self.data_queue)


class ProducerThread(threading.Thread):
    """
    ProducerThread class.
    """
    def __init__(self, cities: list, queue: CityOverheadTimeQueue, thread_num: int):
        """
        Initialize ProducerThread class.
        :param cities: list of City objects
        :param queue: CityOverheadTimeQueue object
        :param thread_num: integer
        """
        super().__init__()
        self.thread_num = thread_num
        self.cities = cities
        self.queue = queue

    def run(self) -> None:
        """
        Run the thread.
        """
        current_time = str(datetime.datetime.now())[11:19]
        index = 0

        for city in self.cities:
            print(f"\n{current_time}: Producer {self.thread_num} is adding to the queue")
            response = ISSDataRequest.get_overhead_pass(city)
            self.queue.put(response)
            print(f"ISSDataRequest for {response.city} element "
                  f"added to queue! Queue has {len(self.queue)} elements")
            index += 1
            if index % 5 == 0:
                print(f"{current_time}: Producer {self.thread_num} is sleeping after producing 5 items")
                time.sleep(1)


class ConsumerThread:
    """
    ConsumerThread class.
    """
    def __init__(self, queue: CityOverheadTimeQueue):
        """
        Initialize ConsumerThread class.
        :param queue: CityOverheadTimeQueue object
        """
        self.queue = queue
        self.data_incoming = True

    def set_data_incoming(self, value: bool) -> None:
        """
        Set new value to the data_incoming attribute.
        :param value: boolean
        """
        self.data_incoming = value

    def run(self) -> None:
        """
        Run the thread.
        """
        current_time = str(datetime.datetime.now())[11:19]
        while self.data_incoming or len(self.queue) > 0:
            if len(self.queue) == 0:
                time.sleep(0.75)
            print(f"element removed from queue! Queue has {len(self.queue)} elements left")
            print(f"{current_time}: Consumer 1 is consuming from the queue")
            overhead_obj = self.queue.get()
            print("---------")
            print(overhead_obj)
            print("---------")
            time.sleep(0.5)


def main():
    filename = "city_locations.xlsx"
    overhead_queue = CityOverheadTimeQueue()
    city_database = CityDatabase(filename)

    city1 = []
    city2 = []
    city3 = []

    for city in city_database.city_db:
        if len(city1) <= len(city2) and len(city1) <= len(city3):
            city1.append(city)
        elif len(city2) < len(city1) and len(city2) == len(city3):
            city2.append(city)
        elif len(city3) < len(city2):
            city3.append(city)

    producer_thread = ProducerThread(city1, overhead_queue, 1)
    producer_thread2 = ProducerThread(city2, overhead_queue, 2)
    producer_thread3 = ProducerThread(city3, overhead_queue, 3)
    consumer_thread = ConsumerThread(overhead_queue)

    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #     for index in range(1, 4):
    #         executor.submit(producer_thread.run, index)
    thread1 = threading.Thread(target=producer_thread.run)
    thread2 = threading.Thread(target=producer_thread2.run)
    thread3 = threading.Thread(target=producer_thread3.run)
    consumer_threading = threading.Thread(target=consumer_thread.run)

    thread1.start()
    thread2.start()
    thread3.start()
    consumer_threading.start()

    thread1.join()
    thread2.join()
    thread3.join()
    consumer_thread.set_data_incoming(False)
    consumer_threading.join()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    duration = end - start
    print(f"Total duration {duration} seconds")





