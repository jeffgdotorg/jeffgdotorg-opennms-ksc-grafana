#!/usr/bin/env python3

rpn_exprs_dict = {
  'out,-1,*': 'out * -1',
  'octIn,8,*': 'octIn * 8',
  'octOut,8,*': 'octOut * 8',
  '0,rawbitsOut,-': '0 - rawbitsOut',
  'octIn,UN,0,octIn,IF': '(octIn == NaN) ? 0 : octIn',
  'octOut,UN,0,octOut,IF': '(octOut == NaN) ? 0 : octOut',
  'bytesOut,{diffTime},*': 'bytesOut * (__diff_time / 1000)',
  'bytesIn,{diffTime},*': 'bytesIn * (__diff_time / 1000)',
  'outSum,inSum,+': 'outSum + inSum',
  '0,avgBusy,GT,0,avgBusy,IF': '(avgBusy > 0) ? avgBusy : 0',
  '10,avgBusy,GT,0,avgBusy,IF': '(avgBusy > 10) ? avgBusy : 0',
  '20,avgBusy,GT,0,avgBusy,IF': '(avgBusy > 20) ? avgBusy : 0',
  '30,avgBusy,GT,0,avgBusy,IF': '(avgBusy > 30) ? avgBusy : 0',
  '40,avgBusy,GT,0,avgBusy,IF': '(avgBusy > 40) ? avgBusy : 0',
  '50,avgBusy,GT,0,avgBusy,IF': '(avgBusy > 50) ? avgBusy : 0',
  '60,avgBusy,GT,0,avgBusy,IF': '(avgBusy > 60) ? avgBusy : 0',
  '70,avgBusy,GT,0,avgBusy,IF': '(avgBusy > 70) ? avgBusy : 0',
  '80,avgBusy,GT,0,avgBusy,IF': '(avgBusy > 80) ? avgBusy : 0',
  '90,avgBusy,GT,0,avgBusy,IF': '(avgBusy > 90) ? avgBusy : 0',
  'memFree,memUsed,+': 'memFree + memUsed',
  'discardsIn,upktsIn,mcpktsIn,+,bcpktsIn,+,/,100,*': 'discardsIn / (upktsIn + mcpktsIn + bcpktsIn) * 100',
  'discardsOut,upktsOut,mcpktsOut,+,bcpktsOut,+,/,100,*': 'discardsOut / (upktsOut + mcpktsOut + bcpktsOut) * 100',
  '0,percentOut,-': '0 - percentOut',
  '0,octOut,-': '0 - octOut'
}

def jexl_for_rpn(rpn):
  if rpn is None:
    return None
  if rpn in rpn_exprs_dict:
    return rpn_exprs_dict[rpn]
  else:
    print("No entry for '" + rpn + "', returning input")
    return rpn
