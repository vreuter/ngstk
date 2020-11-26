""" Functions related to file type """

import os

__author__ = "Vince Reuter"
__credits = ["Vince Reuter"]


__all__ = ["get_mark_duplicates"]


def get_mark_duplicates_spark(in_bam, out_bam, metrics_file)


def get_mark_duplicates(in_bam, out_bam, metrics_file, keep_duplicates, jarfile):
	"""
	Mark duplicate reads with Picard.

	Parameters
	----------
	in_bam : str
		Input BAM file
	out_bam : str
		Output BAM file
	metrics_file : str
		Path to which to write duplicate marking metrics
	keep_duplicates : bool
		Whether to retain duplicates and mark as such, or remove entirely
	jarfile : str
		Path to Picard JAR file

	Returns
	-------
	str
		Command to run to mark duplicates
	"""
	cmd = "java -jar {J} MarkDuplicates I={I} O={O} M={M}".format(J=jarfile, I=in_bam, O=out_bam, M=metrics_file)
	return cmd if keep_duplicates else "{} {}".format(cmd, "REMOVE_DUPLICATES=true")
