import vertica_sdk
from string import printable

class split_printable_idx(vertica_sdk.TransformFunction):
    def processPartition(self, server_interface, arg_reader, res_writer):
        server_interface.log("Split a Varchar and represent it using ASCII indexes of the first 1280 elements")
        while(True):
            x = "" if arg_reader.isNull(0) else arg_reader.getString(0)
            n = len(x)
            for i in range(1280):
                idx = printable.index(x[i]) if i < n else 0
                res_writer.setInt(i, idx)
            res_writer.next()
            if not arg_reader.next():
                break

class split_printable_idx_factory(vertica_sdk.TransformFunctionFactory):
    
    def createTransformFunction(cls, server_interface):
        return split_printable_idx()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        for i in range(1280):
            return_type.addInt()

    def getReturnType(self, srv_interface, arg_types, return_type):
        for i in range(1280):
            return_type.addInt("str_idx{}".format(i))