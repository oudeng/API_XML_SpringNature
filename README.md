# API_XML_SpringNature
Python program for searching info from Springer Nature via API by XML.

Created on Sun May 17 17:24:43 2020
Search in Spring Nature using API by keywords for NIS lab reserch projects.
@author oudeng, Graduate School of Human Sciences, Waseda University
Python program for searching info from Springer Nature via API by XML.
Results includes the title, pdf url and abstract of destination articles. 
https://dev.springernature.com/signup.  
registerred by WasedaID of Ou,DENG, got necessary API.

How to use?

0) Please registered your API key for SpringerNature, easily at following url. Then put it in Python code "api_key". Easily find the place if you review the code.
   https://www.springernature.com/gp/campaign/librarian-covid-tdm?sap-outbound-id=64AF2B62DCE26C591DAA9263090CDAF763E0CD1F
1) Run this program in Python eviroment, including bs4 and requests lib.
2) Input keywords for searching.
3) Searching results will in Python console window.
4) Read in console window directly if not too many results,
   or copy contents to any other more confortable browsers.
5) Copy url of artitle you like in results, use broswer to read PDF.
 
Can use for other API?

Yes. By modifying base_url, api_key, total and content identification tags.
Just confirm the url you try in other API. 

Can for JSON?

No, this programe for XML only.
