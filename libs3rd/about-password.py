from passlib.hash import ldap_salted_sha1 as lsm

hash = lsm.hash('shit')


print(lsm.verify('shits', hash))