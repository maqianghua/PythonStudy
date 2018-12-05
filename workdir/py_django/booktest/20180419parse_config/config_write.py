#!/user/local/bin/python2.7
#encoding:utf-8

from configobj import ConfigObj
config = ConfigObj()
config.indent_type='\t'
config.filename = "WDL.cfg"

#
config["Hadoop"]={}
config["Hadoop"]["HadoopSZ"]="/hwfssz1/BIGDATA_COMPUTING/hadoop/job_submit/10.1.0.51/CDH/bin/hadoop"
config["Hadoop"]["HadoopGB"] = "/hwfssz1/BIGDATA_COMPUTING/hadoop/job_submit/10.53.20.169/CDH/bin/hadoop"
config["Hadoop"]["HadoopMaster"] = "/bin/hadoop"
#
config["streaming"]={}
config["streamingJar"]["streamingJar"]="/hwfssz1/BIGDATA_COMPUTING/hadoop/hadoop/TaskSubmit/10.1.0.51/CDH-5.12.0-1.cdh5.12.0.p0.29/jars/hadoop-streaming-2.6.0-cdh5.12.0.jar"
config["streamingJar"]["streamingJarGB"]=""
config["streamingJar"]["streamingJarMaster"]="/opt/cloudera/parcels/CDH/jars/hadoop-streaming-2.6.0-cdh5.11.1.jar"

#
config["hg19"]={}
config["hg19"]["hg19ref"]="/hwfssz1/BIGDATA_COMPUTING/GaeaProject/reference/hg19/hg19.fasta"
config["hg19"]["hg19bed"] = "/hwfssz1/BIGDATA_COMPUTING/.classpathGaeaProject/reference/hg19/split_bed_75/bed.list"
config["hg19"]["hg19bn"] = "/hwfssz1/BIGDATA_COMPUTING/GaeaProject/reference/hg19/reference/ref_bn.list"
config["hg19"]["dbsnphg19"] = "/hwfssz1/BIGDATA_COMPUTING/GaeaProject/resource/hg19/dbsnp_138.hg19.sort.vcf"
config["hg19"]["annoconfighg19"] = "/hwfssz1/BIGDATA_COMPUTING/bigdata_autoanalysis/support_script/annotation_file/config_hg19.properties"
#
config["hg38"]={}
config["hg38"]["hg38ref"]="/hwfssz1/BIGDATA_COMPUTING/GaeaProject/reference/hg38/hg38.fa"
config["hg38"]["hg38bed"] = "/hwfssz1/BIGDATA_COMPUTING/GaeaProject/reference/hg38/bed_split/bed.list"
config["hg38"]["hg38bn"] = "/hwfssz1/BIGDATA_COMPUTING/GaeaProject/reference/hg38/reference/ref_bn.list"
config["hg38"]["dbsnphg38"] = "/hwfssz1/BIGDATA_COMPUTING/GaeaProject/resource/hg38_sort/dbsnp_138.hg38.sort.vcf"
config["hg38"]["annoconfighg38"] = "/hwfssz1/BIGDATA_COMPUTING/bigdata_autoanalysis/support_script/annotation_file/config_hg38.properties"
#
config["hg37"]={}
config["hg37"]["hg37ref"]="/hwfssz1/BIGDATA_COMPUTING/GaeaProject/reference/hs37d5/hs37d5.fa"
config["hg37"]["hg37bed"] = "/hwfssz1/BIGDATA_COMPUTING/GaeaProject/reference/hs37d5/bed_split/bed.list"
config["hg37"]["hg37bn"] = "/hwfssz1/BIGDATA_COMPUTING/GaeaProject/reference/hs37d5/reference/ref_bn.list"
config["hg37"]["dbsnphg37"] = "/hwfssz1/BIGDATA_COMPUTING/GaeaProject/resource/hs37d5/dbSNP_150.vcf"

#
config["hg38nalt"]={}
config["hg38nalt"]["hg38naltref"]="/hwfssz1/BIGDATA_COMPUTING/GaeaProject/reference/hg38_noalt_withrandom/hg38.fa"
config["hg38nalt"]["hg38naltbed"] = "/hwfssz1/BIGDATA_COMPUTING/GaeaProject/reference/hg38_noalt_withrandom/bed_split/bed.list"
config["hg38nalt"]["hg38naltbn"] = "/hwfssz1/BIGDATA_COMPUTING/GaeaProject/reference/hg38_noalt_withrandom/reference/ref_bn.list"
config["hg38nalt"]["dbsnphg38nalt"] = "/hwfssz1/BIGDATA_COMPUTING/GaeaProject/resource/hg38_noalt_withrandom/dbsnp_138.hg38_noalt_withrandom.vcf"
config["hg38nalt"]["dbsnphg38nalt"] = "/hwfssz1/BIGDATA_COMPUTING/GaeaProject/resource/hg38_noalt_withrandom/dbsnp_138.hg38_noalt_withrandom.vcf"
#
config["AnoConfig"]={}
config["AnoConfig"]["annoconfighg19"]="/hwfssz1/BIGDATA_COMPUTING/bigdata_autoanalysis/support_script/annotation_file/config_hg19.properties"


