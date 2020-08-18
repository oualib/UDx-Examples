import vertica_sdk
from string import printable

class printable_idx(vertica_sdk.ScalarFunction):
    """Return the sum of two integer columns"""

    def __init__(self):
        pass
    def setup(self, server_interface, col_types):
        pass
    def processBlock(self, server_interface, arg_reader, res_writer):
        server_interface.log("Print the ASCII index of the first char of a varchar")
        while(True):
            if arg_reader.isNull(0):
                idx = 0
            else:
                x = arg_reader.getString(0)
                idx = printable.index(x[0]) if (len(x) > 0) else 0
            res_writer.setInt(idx)
            res_writer.next()
            if not arg_reader.next():
                break
    def destroy(self, server_interface, col_types):
        pass

class printable_idx_factory(vertica_sdk.ScalarFunctionFactory):
    
    def createScalarFunction(self, srv):
        return printable_idx()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addInt()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addInt()