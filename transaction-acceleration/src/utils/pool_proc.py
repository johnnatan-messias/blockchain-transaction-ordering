from multiprocessing import JoinableQueue, Process, Queue

from .logger_factory import LoggerFactory

logger = LoggerFactory.get_logger('logger_application')


class Worker(Process):
    def __init__(self, tasks, results, save_results):
        Process.__init__(self)
        self.tasks = tasks
        self.results = results
        self.__end = False
        self.daemon = True
        self.save_results = save_results
        self.start()

    def run(self):
        while not self.__end:
            func, args, kargs = self.tasks.get()
            try:
                if self.save_results:
                    self.results.put(func(*args, **kargs))
                else:
                    func(*args, **kargs)
            except:
                logger.error("Error on Worker", exc_info=True)
            self.tasks.task_done()

    def end_(self):
        self.__end = True


class Pool:
    def __init__(self, n_processes, save_results=True):
        self.tasks = JoinableQueue(n_processes)
        self.results = Queue(-1)
        self.save_results = save_results
        self.__workers = list()
        for _ in range(n_processes):
            self.__workers.append(
                Worker(self.tasks, self.results, self.save_results))

    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        self.tasks.join()
        return self

    def terminate(self):
        for worker in self.__workers:
            worker.end_()
            worker.terminate()
            worker.join()

    def get_results(self):
        while not self.results.empty():
            yield self.results.get()
