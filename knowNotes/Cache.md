# Cache

## Memcached
[official defination](https://memcached.org/about)

It abstracts the memory of the computer and make that part of memory public to the applications. The shared memory is more like a shared fast database which can tempararily store the data.
Without memcached, the memory for each application is seperated and memcache can never share between the nodes/replicas. But with this, memcached published a chunck of memory so all the nodes can access the same memory for data.


