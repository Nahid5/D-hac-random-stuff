//https://d-hac.github.io/puzzle/chemistry-spelling
/*
 Nahid Sarker
 The python file has a webscraper to get all the chemical symbols and spelling
  
  Today’s goal is to spell user-inputted words with elements from the periodic table by using their 1-2 letter chemical symbol. For example, given the input:
luck
functions
bacon
poison
sickness
ticklish

The program should output:

LuCK (lutetium, carbon, potassium)
FUNCTiONS (flourine, uranium, nitrogen, carbon, titanium, oxygen, nitrogen, sulfur)
BaCoN (barium, cobalt, nitrogen)
POISON (phosphorus, oxygen, iodine, sulfur, oxygen, nitrogen)
SiCKNeSS (silicon, carbon, potassium, neon, sulfur, sulfur)
TiCKLiSH (titanium, carbon, potassium, lithium, sulfur, hydrogen)
  
 */
package chem;
import java.util.*;


public class ChemSpelling 
{
	public static void main (String args[])
	{
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Enter in the word");
		String word = scan.nextLine();
		word.toLowerCase();
		
		for (int i = 0; i < word.length(); ++i)
		{
			String upToFirst = word.substring(i, 1+i);
			String upToThird = " ";
			String upToSecond = " ";
			
			//these 2 if prevent index out of bound error
			if (i + 3 < word.length())
			{
				upToThird = word.substring(i, 3+i);
			}
			if (i + 2 < word.length())
			{
				upToSecond = word.substring(i, 2+i);
			}
			
			//check if the letters can make a chemical
			if (inTable(upToThird) != null)
			{
				System.out.println(inTable(upToThird));
				i += 2;
			}
			else if (inTable(upToSecond) != null)
			{
				System.out.println(inTable(upToSecond));
				i += 1;
			}
			else if (inTable(upToFirst) != null)
			{
				System.out.println(inTable(upToFirst));
			}
			else
			{
				System.out.println("No Chemicles found");
			}
		}
	}
	
	//a map with symbol as the key and the spelling with the value
	public static String inTable(String symbol)
	{
		Map <String, String> map = new HashMap<String, String>();
		//map was created using web scraper in python
		map.put("h", "Hydrogen");
		map.put("he", "Helium");
		map.put("li", "Lithium");
		map.put("be", "Beryllium");
		map.put("b", "Boron");
		map.put("c", "Carbon");
		map.put("n", "Nitrogen");
		map.put("o", "Oxygen");
		map.put("f", "Fluorine");
		map.put("ne", "Neon");
		map.put("na", "Sodium");
		map.put("mg", "Magnesium");
		map.put("al", "Aluminum");
		map.put("si", "Silicon");
		map.put("p", "Phosphorus");
		map.put("s", "Sulfur");
		map.put("cl", "Chlorine");
		map.put("ar", "Argon");
		map.put("k", "Potassium");
		map.put("ca", "Calcium");
		map.put("sc", "Scandium");
		map.put("ti", "Titanium");
		map.put("v", "Vanadium");
		map.put("cr", "Chromium");
		map.put("mn", "Manganese");
		map.put("fe", "Iron");
		map.put("co", "Cobalt");
		map.put("ni", "Nickel");
		map.put("cu", "Copper");
		map.put("zn", "Zinc");
		map.put("ga", "Gallium");
		map.put("ge", "Germanium");
		map.put("as", "Arsenic");
		map.put("se", "Selenium");
		map.put("br", "Bromine");
		map.put("kr", "Krypton");
		map.put("rb", "Rubidium");
		map.put("sr", "Strontium");
		map.put("y", "Yttrium");
		map.put("zr", "Zirconium");
		map.put("nb", "Niobium");
		map.put("mo", "Molybdenum");
		map.put("tc", "Technetium");
		map.put("ru", "Ruthenium");
		map.put("rh", "Rhodium");
		map.put("pd", "Palladium");
		map.put("ag", "Silver");
		map.put("cd", "Cadmium");
		map.put("in", "Indium");
		map.put("tin", "In");
		map.put("sn", "Tin");
		map.put("sb", "Antimony");
		map.put("te", "Tellurium");
		map.put("i", "Iodine");
		map.put("xe", "Xenon");
		map.put("cs", "Cesium");
		map.put("ba", "Barium");
		map.put("la", "Lanthanum");
		map.put("ce", "Cerium");
		map.put("pr", "Praseodymium");
		map.put("nd", "Neodymium");
		map.put("pm", "Promethium");
		map.put("sm", "Samarium");
		map.put("eu", "Europium");
		map.put("gd", "Gadolinium");
		map.put("tb", "Terbium");
		map.put("dy", "Dysprosium");
		map.put("ho", "Holmium");
		map.put("er", "Erbium");
		map.put("tm", "Thulium");
		map.put("yb", "Ytterbium");
		map.put("lu", "Lutetium");
		map.put("hf", "Hafnium");
		map.put("ta", "Tantalum");
		map.put("w", "Tungsten");
		map.put("re", "Rhenium");
		map.put("os", "Osmium");
		map.put("ir", "Iridium");
		map.put("pt", "Platinum");
		map.put("au", "Gold");
		map.put("hg", "Mercury");
		map.put("tl", "Thallium");
		map.put("pb", "Lead");
		map.put("bi", "Bismuth");
		map.put("po", "Polonium");
		map.put("at", "Astatine");
		map.put("rn", "Radon");
		map.put("fr", "Francium");
		map.put("ra", "Radium");
		map.put("ac", "Actinium");
		map.put("th", "Thorium");
		map.put("pa", "Protactinium");
		map.put("u", "Uranium");
		map.put("np", "Neptunium");
		map.put("pu", "Plutonium");
		map.put("am", "Americium");
		map.put("cm", "Curium");
		map.put("bk", "Berkelium");
		map.put("cf", "Californium");
		map.put("es", "Einsteinium");
		map.put("fm", "Fermium");
		map.put("md", "Mendelevium");
		map.put("no", "Nobelium");
		map.put("lr", "Lawrencium");
		map.put("rf", "Rutherfordium");
		map.put("db", "Dubnium");
		map.put("sg", "Seaborgium");
		map.put("bh", "Bohrium");
		map.put("hs", "Hassium");
		map.put("mt", "Meitnerium");
		map.put("ds", "Darmstadtium");
		map.put("rg", "Roentgenium");
		map.put("uub", "Ununbium");
		map.put("uut", "Ununtrium");
		map.put("uuq", "Ununquadium");
		map.put("uup", "Ununpentium");
		map.put("uuh", "Ununhexium");
		map.put("uus", "Ununseptium");
		map.put("uuo", "Ununoctium");
		return map.get(symbol);
	}
}
