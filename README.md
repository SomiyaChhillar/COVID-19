# India  COVID-19 🦠 Data Scrape

Data scraping is done using **BeautifulSoup** and **requests**. Data has been scraped from **[MohHFW](https://www.mohfw.gov.in/)** website, the official website for COVID-19 for India. 

# Heat Map
Libraries used : Geopandas and Matplotlib

    country = geopandas.read_file('India/Indian_States.shp')
	ax = country.plot(column='total_cases', legend=True)


# Environment 💻

The envirnoment can be created using Anaconda in both Linux and Windows. Versions for packages might be different for them. The file covid.yml is set up in a Windows system.

To create the same environment:

    conda env create -f covid.yml
To activate the environment:

    conda  activate  ytscrape

# Contact 📞      
Feel free to fork 🍴 the repository. 

📧 Email me at rishabh080598@gmail.com for collaboration of you can also reach out to me on 💬 [LinkedIn](https://www.linkedin.com/in/rishabh98/) .

