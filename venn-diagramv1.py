import streamlit as st
from matplotlib_venn import venn2, venn2_circles
from matplotlib import pyplot as plt

def main():
    st.title("Venn Diagram Generator")

    # Input for sets
    st.subheader("Enter the elements for each set")
    set1 = st.text_input("Set A (comma-separated values)", "1,2,3")
    set2 = st.text_input("Set B (comma-separated values)", "2,3,4")

    # Convert input strings to sets
    set_a = set(set1.split(','))
    set_b = set(set2.split(','))

    # Button to generate Venn diagram
    if st.button("Generate Venn Diagram"):
        fig, ax = plt.subplots()
        venn2([set_a, set_b], set_labels=('A', 'B'), ax=ax)
        venn2_circles([set_a, set_b], ax=ax)
        
        # Display the diagram
        st.pyplot(fig)

if __name__ == "__main__":
    main()
