# Speech to Text


## Design
The overall design consists of a multiprocessing and multithreading system.

Each API call will spawn a new process; therefore, processes will be created just for the modules. 
In order to find the number of API calls to run simultaneously, I will perform a CPU analysis to find the bottleneck of the system when calling all APIs.

At the same time, the system will support multiple threads by splitting API functionality into multiple threads.
The number of threads will depend on the number of functions of each API.



Schedule api requests (text to speech)
Assuming same priority 
Will use FIFO queue 


Design: Establish a processing criteria:
How many API calls you can handle simultaneously and why?
For example, run different API calls at the same time?
Split the processing of an API into multiple threads or processes?

Will have 1 process per module or
How many processes? → Need to do CPU analysis/find the bottleneck of the system when calling all APIs
Spawn a process with each api call
Therefore, will have a system that supports multiple processes
At the same time, the system will support multiple threads by splitting API functionality into threads
How many threads? → depends on the functions of each API (1 thread per inner function)
Ie. speech to text will have 
