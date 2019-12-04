
custom = {

}


defaults = {
    "abs": abs,
    "range": range,
    "abs": abs,
    "dict": dict,
    "min": min,
    "all": all,
    "hex": hex,
    "next": next,
    "slice": slice,
    "any": any,
    "divmod": divmod,
    "object": object,
    "sorted": sorted,
    "ascii": ascii,
    "enumerate": enumerate,
    "input": input,
    "oct": oct,
    "bin": bin,
    "int": int,
    "str": str,
    "bool": bool,
    "isinstance": isinstance,
    "ord": ord,
    "sum": sum,
    "bytearray": bytearray,
    "filter": filter,
    "issubclass": issubclass,
    "pow": pow,
    "bytes": bytes,
    "float": float,
    "iter": iter,
    "tuple": tuple,
    "callable": callable,
    "format": format,
    "len": len,
    "property": property,
    "type": type,
    "chr": chr,
    "frozenset": frozenset,
    "list": list,
    "range": range,
    "locals": locals,
    "repr": repr,
    "zip": zip,
    "map": map,
    "reversed": reversed,
    "complex": complex,
    "max": max,
    "round": round
}

imports = {**custom, **defaults}


# bypass for tests
imports["bypass"] = True
