"""
Created on Apr 10 14:25 2019

@author: nishit
"""
import struct

from src.utils.updDataConversion import UDPDataConversion

data = b'\x00\x00\x00\x00Bk\x1b\x82B!}uB\x9e\x97iB\x93\xe5\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\x80\x00\x00?\x80\x00\x00?\x80\x00\x00?\x80\x00\x00E\xec\x87CE\xda\xa2\xd7E\x91\xd3%E\xa8P\x19D\x01\xa0\xccD\x06\xa1\xe7D\t\xa2~C\xc5y\xfe>a\xd6\x13>a\xb3c>a\xd7f>b\x10\xec<^|\xb0<^|\xaa<^|\xab<^|\xb69Q\xb7\x179Q\xb7\x179Q\xb7\x179Q\xb7\x17;\xf4NI;\xf4Wq;\xf36=;\xf24\x1b\xb5\xa1g\xd3\xb5\xa0\xa0+\xb5\x9f\xe3L\xb5\xa1\xc9\xb4\xa2r\xc5\x10>\x08\xb8\x06>\x82y\x88>\xa0\xf4\x00?\x80\x00\x00?\x80\x00\x00?\x80\x00\x00?\x80\x00\x009Q\xb7\x179Q\xb7\x179Q\xb7\x179Q\xb7\x17F\x9d\xe9\x85CK$^B|d\xb2C\x9d\x14\xf9C\x9d\x14`C\x9d\x13\xe4C\x9d\x13\x88'

l = UDPDataConversion.convert_from_udf_data(data, 60)

d = UDPDataConversion.convert_to_udf_data(l)
print(l)
print(data)
print(d)

d = b'\x00\x00\x00\x00Bk\x1b\x82B!}uB'
i = 1
e = d[(4 * i):(4 + 4 * i)]
print(e)
f = struct.unpack(">f", e)[0]
g = struct.pack(">f", f)
print(f)
print(g)