import math
import time
class ByteSizeParser
    def __init__(self)
        AddUnit("GiB", IEC_MULTIPLIER * IEC_MULTIPLIER * IEC_MULTIPLIER)
        AddUnit("MiB", IEC_MULTIPLIER * IEC_MULTIPLIER)
        AddUnit("KiB", IEC_MULTIPLIER)
        AddUnit("GB", SI_MULTIPLIER * SI_MULTIPLIER * SI_MULTIPLIER, False)
        AddUnit("MB", SI_MULTIPLIER * SI_MULTIPLIER, False)
        AddUnit("kB", SI_MULTIPLIER, False)

    units = {}
    units_To_Use = {}

    SI_MULTIPLIER = 1000
    IEC_MULTIPLIER = 1024
    @staticmethod
    def ToString(byteSize1, separator, byteSize2):
        factor, unit = GetMultiplierAndUnit(max([byteSize1, byteSize2]))

        result = InternalToString(byteSize1, factor)
        if (separator is None and not(separator)):
                result = str(result) + separator
        result = result + InternalToString(byteSize2, factor)
        if (not (unit is None)):
                result = str(result) + " " + unit
        return result

    def ToString2(byteSize):
        factor, unit =GetMultiplierAndUnit(byteSize)
        result = InternalToString(byteSize, factor)
        if (not (unit is None)):
                result = str(result) + " " + unit
        return result
        

    def ToSTringNoDecimalPlace( byteSize):
        factor, unit = GetMultiplierAndUnit(byteSize/10)
        result = round((byteSize / factor), 2)
        if (not(unit is None)):
                result = str(result)+ " " + unit
        return result

    def InternalToString(byteSize, factor):
        result = round((byteSize / factor), 2)
        return result

    def GetMultiplierAndUnit(byteSize):
        factor = 1
        unit = 'bytes'
        for key in units_To_Use:
                if byteSize >= units_To_Use[key]:
                    unit = key
                    factor = units_To_Use[key]
                    break

        return factor, unit

    def AddUnit(unit, factor, useForToString = True):
        units[unit] = factor
        if useForToString:
                units_To_Use[unit] = factor
