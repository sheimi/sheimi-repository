package me.sheimi.mapred;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.SequenceFileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Test {
	public static class TestMapper extends
			Mapper<Text, BytesWritable, Text, BytesWritable> {
		public void map(Text key, BytesWritable value, Context context) {
			System.err.println(key.toString());
			try {
				context.write(key, value);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
	public static class TestReducer extends Reducer<Text, BytesWritable, Text, IntWritable> {
		IntWritable iw = new IntWritable();
		public void reduce(Text key, Iterable<BytesWritable> values, Context context) {
			int i = 0;
			for (BytesWritable value : values) {
				i += value.get().length;
			}
			iw.set(i);
			try {
				context.write(key, iw);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
	public static void main(String[] args) throws IOException,
			InterruptedException, ClassNotFoundException {
		Configuration conf = new Configuration();
		
		Job job = new Job(conf, "test");
		Path input = new Path("/test/input");
		Path output = new Path("/test/output");
		
		job.setJarByClass(Test.class);
		job.setMapperClass(TestMapper.class);
		job.setReducerClass(TestReducer.class);
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(BytesWritable.class);
		job.setInputFormatClass(SequenceFileInputFormat.class);
		
		FileInputFormat.addInputPath(job, input);
		FileOutputFormat.setOutputPath(job, output);
		
		int exit_code = job.waitForCompletion(true) ? 0 : 1;
		System.exit(exit_code);
	}
}
