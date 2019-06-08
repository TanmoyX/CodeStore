import java.util.*; 

class Unique{ 
	boolean uniqueCharacters(String str) 
	{ 
		int checker = 0; 

		for (int i = 0; i < str.length(); i++) { 
            System.out.println(checker);
			int bitAtIndex = str.charAt(i) - 'a'; 

			// if that bit is already set in checker, 
			// return false 
			if ((checker & (1 << bitAtIndex)) > 0) 
				return false; 

			// otherwise update and continue by 
			// setting that bit in the checker 
			checker = checker | (1 << bitAtIndex); 
		} 

		// no duplicates encountered, return true 
		return true; 
	} 
} 