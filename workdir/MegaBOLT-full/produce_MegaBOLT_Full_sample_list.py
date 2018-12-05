#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
produce_sample_list.py--This program is used for generate MegaBOLT-full sample.list
@author:    maqianghua
@copyright: 2018 BGI BigData.   All rights reserved.
@contact:   maqianghua@genomics.cn
@deffield:  updated:Updated
'''
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
import os
import sys
import signal

__all__=[]
__version__='1.0.0 beta'
__date__='2018-7-23'
__updated__='2018-7-23'

DEBUG=0
TESTRUN=0
PROFILE=0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self,msg):
        super(CLIError).__init__(type(self))
        self.msg="E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def run(args):
    with open('%s' % args.sampleList,'r') as sampleList_fn:
        list_sample_info= sampleList_fn.readlines()
    with open('%s' % args.outputFile,'w') as outputFile_fn:
        read_1=''
        read_2=''
        length=len(list_sample_info)
        for i in range(length):
            if (i%2)==0:
                read_1=read_1+list_sample_info[i].strip()+','
            else:
                read_2=read_2+list_sample_info[i].strip()+','
        outputFile_fn.write('%s\t%s\t%s\t%s\t%s' % (args.sampleName,read_1.strip(','),read_2.strip(','),args.adapter1,args.adapter2))


def single_run(args):
    with open('%s' % args.sampleList,'r') as sampleList_fn:
        list_sample_info= sampleList_fn.readlines()
    with open('%s' % args.outputFile,'w') as outputFile_fn:
        read_1=[]
        read_2=[]
        length=len(list_sample_info)
        for i in range(length):
            if (i%2)==0:
                read_1.append(list_sample_info[i].strip())
            else:
                read_2.append(list_sample_info[i].strip())
        for j in range(length/2):
            outputFile_fn.write('%s_%d,%s,%s,%s,%s,%s\n' % (args.sampleName,j,args.sampleName,args.library,args.platform,read_1[j],read_2[j]))
def parse_boolean(s):
    if s.upper()=="TRUE":
       return True
    elif s.upper()=="FALSE":
       return False
    else :
	   raise RuntimeError('string value is not False or True, please check it! ')

def main(argv=None):#INGORE:COlll
    '''Command line options.'''
    if argv is None:
        argv=sys.argv
    else:
        sys.argv.extend(argv)

    program_name=os.path.basename(sys.argv[0])
    program_version='v%s' % __version__
    program_build_date=str(__updated__)
    program_version_message='%%(prog)s %s (%s)' % (program_version, program_build_date)
    # program_shortdesc=__import__('__main__').__doc__.split["\n"][1]
    program_shortdesc='produce_sample_list.py--This program is used for generate MegaBOLT-full sample.list'
    program_license='''%s
    Created by maqianghua on %s.
    Copyright 2018 BGI bigData. All rights reserved.
USAGE
''' %(program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser=ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-sm","--sampleName",dest="sampleName",help="The name of the sample",required=True)
        parser.add_argument("-s","--sampleList",dest="sampleList",help="a list of sample information, one sample of each row",required=True)
        parser.add_argument("-PL","--platform",dest="platform",type=str,default="None",help="The sequence platform of sample,if -f parameter is False, this parameter is required ")
        parser.add_argument("-LB","--library",dest="library",type=str,default="None",help="The Library of sample,if -f parameter is False, this parameter is required")
        parser.add_argument("-a1","--adapter1",dest="adapter1",help="The adapter of read1 ,if -f parameter is true, this parameter is required")
        parser.add_argument("-a2","--adapter2",dest="adapter2",help="The adapter of read2,if -f parameter is true, this parameter is required")
        parser.add_argument("-f","--MegaBOLTfull",action="store_true",default=False,help="use MegaBOLTfull to analysis.[default: %(default)s]")
        parser.add_argument("-o","--outputFile",dest="outputFile",help="The result of file",required=True)

        # Process arguments
        args=parser.parse_args()
        if not os.path.exists(os.path.abspath(args.sampleList)):
            raise  RuntimeError("%s: No such file or directory." % args.sampleList)
        if args.MegaBOLTfull:
            #if args.adapter1 and args.adapter2:
            #    raise RuntimeError("%s :run MegaBOLTfull must include adapter of sample")
            run(args)
        else:
            single_run(args)

        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 1
    except Exception as e:
        if DEBUG or TESTRUN:
            raise (e)

        # statedir = impl.mkdir(args.workdir, 'scripts', 'state')
        # with open(os.path.join(statedir, 'failed'), 'w') as f:
        #     f.write('generate scripts failed. please check your sample mode!')

        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2
def wfc_signal_handler(signum, frame):
    print ('Signal handler called with signal', signum)
    raise RuntimeError('Signal handler called with signal '+str(signum))
if __name__ == '__main__':
    # main()
    signal.signal(signal.SIGBUS, wfc_signal_handler)
    signal.signal(signal.SIGSEGV, wfc_signal_handler)
    signal.signal(signal.SIGILL, wfc_signal_handler)
    signal.signal(signal.SIGFPE, wfc_signal_handler)
    if DEBUG:
        sys.argv.append("-h")
        sys.argv.append("-r")
    if TESTRUN:
        import doctest

        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats

        profile_filename = 'testArg_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())
