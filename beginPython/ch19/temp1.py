from ConfigParser import ConfigParser

cf = ConfigParser()
cf.read("test.conf")
secs = cf.sections()
print ('sections:', secs)
opts = cf.options('a')
print ('options:', opts)
kvs = cf.items('a')
print ('sec_a:', kvs )

cf.set("b", "b_key3", "new-$r")
cf.set("b", "b_newkey", "new-value")
cf.add_section('a_new_section')
cf.set('a_new_section', 'new_key', 'new_value')
cf.write(open("test.conf", "w"))