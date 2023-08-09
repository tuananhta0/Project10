import streamlit as st

khai_vi = ["Griller bread", "Onion Soup", "Salad", "Cold Noodle", "Fry Corn"]
mon_chinh = ["Chicken", "Pizza", "Pad Thai", "Steak", "Paella"]
trang_mieng = ["Ice Cream", "Pudding", "Fruits", "Tiramisu"]

with st.form("Thuc don yeu thich"):
  options1 = st.multiselect("Chon mon khai vi", khai_vi)
  options2 = st.multiselect("Chon mon chinh", mon_chinh)
  options3 = st.multiselect("Chon mon trang mieng", trang_mieng)
  submitted = st.form_submit_button("Submit")

if submitted:
  st.write("Cac mon da duoc chon:")
  st.write("1.Mon khai vi: ")
  if len(options1) == 0:
    st.write("ban chua chon mon khai vi")
  else:
    for i in range(len(options1)):
      st.write(options1[i])

  st.write("2.Mon chinh:")
  if len(options2) == 0:
    st.write("ban chua chon mon chinh")
  else:
    for i in range(len(options2)):
      st.write(options2[i])

  st.write("3.Mon trang mieng:")
  if len(options3) == 0:
    st.write("ban chua chon mon trang mieng")
  else:
    for i in range(len(options3)):
      st.write(options3[i])
