## Conference Talk Proposal

### Speaker Bio

Jasmine Wong [she/her/hers] is a Master's student in Library and Information Science at the University of Illinois at Urbana-Champaign. In her research, she explores themes of representation and bias in the Western literary canon and literary history using Python text mining methods. Outside of academics, she she works to support women and minority entrepreneurs as the Web Designer & Digital Administrator at The Startup Ladies.



### Talk Title

"Making the Zoo Work for You: Python and Pandas for Humanities Data"



### Description

The Pandas Python library can be a powerful tool for visualizing data structures and performing data analysis on unstructured data, as is commonly used in humanities research. However, adopting this tool can present a steep learning curve that may seem impossible to navigate alone. During this talk, we will walk through a short demonstration using real humanities data and several standard but powerful Pandas methods.

In this talk, I will demonstrate how to read in spreadsheet data to build two simple Pandas dataframes, then transform them with the following methods: concat, drop_duplicates, duplicated, and groupby. As we discuss these methods, attendees will also learn the underlying structure and logic of Pandas and build a foundation for expanding their toolkit beyond methods covered in this presentation.

At the conclusion of this talk, attendees completely new to Python and Pandas will be able to implement these methods in their own research.



### Who and Why?

**WHO:**

This talk is specifically designed for humanities scholars new to Python methods and Pandas dataframes, particularly those working with large catalog datasets and semi-structured humanities data. It is intended to give a very brief overview of how Pandas can be used to illustrate data in an interface that is more familiar and approachable to anyone who has used a spreadsheet.

It may attract a broader audience of Python practitioners interested in learning about humanities data manipulation and digital humanities research. It may also be of interest to other Western literary canon scholars and literary historians using digital methods in their research. The speaker hopes that audience members will take the methods discussed and apply them to their own research.

**BACKGROUND:**

Participants are expected to bring a laptop pre-installed with the Jupyter Notebook provided. Experience with Python not required, but understanding of programming logic helpful. Attendees should have basic knowledge of Excel spreadsheets and familiarity with spreadsheet formatting. Data cleaning will be briefly mentioned but not discussed in-depth during this presentation.



### Timing Outline

*(skeleton with rough timing)*

- Brief speaker intro (1min)
- Presentation overview (1min)
  - Share outline and major steps of what we'll be covering (loading data, combining datasets, processing loaded data, combining duplicates, recombining dataframes)
- Caveat: tidy your data! (2min)
  - Mention "Tidy Data" (Wickham 2014)
- My data (1min)
  - Brief snapshot of rough (but cleaned!) data that I'll be working with during the presentation
- What are Pandas? (3min)
  - Why we use Pandas, what Python Pandas can do for you
  - practical demo - import pandas
- Loading CSV data and first look at dataframes (3min)
  - practical demo - .read()
- Combining your datasets into a concatenated dataframe (4min)
  - practical demo - .concat()
- Pulling a sub-dataframe from your concatenated dataframe (4min)
  - practical demo - .duplicated()
- Consolidating duplicated records in your sub-dataframe (4min)
  - practical demo - .groupby()
- Putting everything together with .concat() (3min)
- Exporting data (2min)
  - Practical demo - .to_csv
- Review (2min)



### Additional Notes

Due to time constraints, speaker will create a specialized Jupyter Notebook for this talk that contains sample data that has been tidied further to avoid the need for demonstrating data cleaning methods during the presentation. This is to avoid confusing participants and keep the presentation more streamlined and focused on data processing. Jupyter Notebook will be provided to attendees prior to the presentation, with instructions for installation and brief introduction to Jupyter Notebooks, so participants can follow along with the live demonstration.

Speaker will also develop backup slides to illustrate coding in case live Jupyter Notebook demonstration cannot load.