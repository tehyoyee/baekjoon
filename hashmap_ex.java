// Hashmap.java
// 23.07.17.

import java.util.HashMap;
import java.util.Map;
import java.util.*;

class hashmap_ex {

	public static void main(String[] args) {
		
		Map<String, Integer> map = new HashMap<>();

		// put, get
		// containsKey
		// putAll
		// keySet
		// forEach
		// remove
		// clear
		// size

		// entrySet()
		// getKey()
		// getValue()



		map.put("a", 1);
		map.put("b", 2);
		map.put("c", 3);
		map.put("d", 4);
		map.remove("a");

		for (Map.Entry<String, Integer> entry : map.entrySet()) {
			System.out.println(entry.getKey() + " " + entry.getValue());
		}
		for (String key : map.keySet()) {
			System.out.println(key + " " + map.get(key));
		}
		map.forEach((key, value) ->
		{
			System.out.println("{"+key+", "+value+"}");
		});
	}
}