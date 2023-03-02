import streamlit as st 

st.tittle('rahul ki website')

col,col1=st.columns(2)
with col:
    st.write("Git and GitHub are related but distinct technologies.Git is a version control system that allows developers to manage changes to their code over time. With Git, developers can track changes to their code, collaborate with other developers, and manage different versions of their codebase.GitHub, on the other hand, is a web-based platform that provides a graphical user interface (GUI) on top of Git. It allows developers to store their Git repositories in the cloud and provides additional tools for collaboration, issue tracking, code review, and continuous integration.In short, Git is the underlying technology that provides version control functionality, while GitHub is a web-based platform built on top of Git that provides additional collaboration and project management features.It's worth noting that while GitHub is the most well-known and widely used platform for hosting Git repositories, there are other similar services such as GitLab and Bitbucket ")
    st.checkbox('----',['git','github'])
    st.write('I am kinking my vs code to github probfile that make ease of updating ')