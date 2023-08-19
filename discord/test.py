from lock import *

lock=GlobalLocks().global_lock

lock2=GlobalLocks().global_lock

print(lock is lock2)