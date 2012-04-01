package me.sheimi;

import org.apache.pig.EvalFunc;
import org.apache.pig.backend.executionengine.ExecException;
import org.apache.pig.data.DataByteArray;
import org.apache.pig.data.Tuple;

public class Test extends EvalFunc<Integer> {

	@Override
	public Integer exec(Tuple input) {
		// TODO Auto-generated method stub
		if (input == null || input.size() == 0)
			return null;
		
		try {
			DataByteArray b = ((DataByteArray) input.get(0));
			return b.get().length;
		} catch (ExecException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}

}
