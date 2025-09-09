import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="مشروع معالجة الصور", layout="wide")

# الحالة الافتراضية للصفحات
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- الصفحة الرئيسية ----------
def home_page():
    # الصورة الرئيسية
    main_img = Image.open("PixelWise/Images/G1.png")
    st.image(main_img, use_container_width=True)



    # عدد الدروس
    lessons = [
        "Lesson 1: Digital Image ",
        "Lesson 2: Color Systems",
        "Lesson 3: Pixel Operations",
        "Lesson 4: Filters & Convolution",
        "Lesson 5: Noise Removal",
        "Lesson 6: Edge Detection",
        "Lesson 7: Morphological Operations",
        "Lesson 8: Geometric Transformations"
    ]

    # نرتب الأزرار في صفوف، كل صف يحتوي 3 أزرار
    cols_per_row = 3
    for i in range(0, len(lessons), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, lesson in enumerate(lessons[i:i+cols_per_row]):
            if cols[j].button(lesson):
                st.session_state.page = f"lesson{i+j+1}"  # تحدد الصفحة المفتوحة

# ---------- الدرس الأول ----------
def lesson1_page():
    main_img = Image.open("PixelWise/Images/L1.png")
    st.image(main_img, use_container_width=True)


    uploaded_file = st.file_uploader("Download Photo", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # فتح الصورة
        img = Image.open(uploaded_file)
        img_array = np.array(img)

        # استخراج معلومات
        height, width = img_array.shape[:2]
        channels = 1 if len(img_array.shape) == 2 else img_array.shape[2]
        bit_depth = img_array.dtype

        st.write(f"Dimintions: {width} × {height}")
        st.write(f"Number of channels : {channels}")
        st.write(f"color Depth (bit depth): {bit_depth}")

        # عرض الصورة
        st.image(img, caption="Original photo",  use_container_width=True)

    # زر العودة
    if st.button("⬅️ Back"):
        st.session_state.page = "home"


# ---------- الدرس الثاني ----------
# ---------- الدرس الثاني ----------
# ---------- الدرس الثاني ----------
def lesson2_page():
    main_img = Image.open("PixelWise/Images/L2.png")
    st.image(main_img, use_container_width=True)


    uploaded_file = st.file_uploader("Download Photo", type=["jpg", "png", "jpeg"], key="lesson2_uploader")
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img_array = np.array(img)

        # عرض الصورة الأصلية
        st.image(img, caption="Original photo", use_container_width=True)

        # Gray
        gray = img.convert("L")
        st.image(gray, caption="Image after Gray", use_container_width=True)
        st.download_button(
            label="⬇️ Download Gray",
            data=gray.tobytes(),
            file_name="gray_image.png",
            mime="image/png"
        )

        # HSV
        hsv = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)
        hsv_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
        hsv_img = Image.fromarray(hsv_rgb)
        st.image(hsv_img, caption="Image after HSV", use_container_width=True)
        st.download_button(
            label="⬇️ Download HSV",
            data=hsv_img.tobytes(),
            file_name="hsv_image.png",
            mime="image/png"
        )

        # قنوات R/G/B
        r, g, b = img.split()
        for channel, name in zip([r, g, b], ["R", "G", "B"]):
            st.image(channel, caption=f"Channel {name}", use_container_width=True)
            st.download_button(
                label=f"⬇️ Download channel {name}",
                data=channel.tobytes(),
                file_name=f"{name}_channel.png",
                mime="image/png"
            )

    # زر العودة
    if st.button("⬅️ Back", key="lesson2_back"):
        st.session_state.page = "home"
# ---------- الدرس الثالث ----------
def lesson3_page():
    main_img = Image.open("PixelWise/Images/L3.png")
    st.image(main_img, use_container_width=True)

    uploaded_file = st.file_uploader("Download Image", type=["jpg", "png", "jpeg"], key="lesson3_uploader")
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img_array = np.array(img)

        # عرض الصورة الأصلية
        st.image(img, caption="Original Image", use_container_width=True)

        # تعديل السطوع والعتامة
        st.markdown("###Brightness and Opacity Modification")
        brightness = st.slider("Brightness (beta)", -100, 100, 0)
        contrast = st.slider("Contrast (alpha)", 0.1, 3.0, 1.0)

        modified_array = cv2.convertScaleAbs(img_array, alpha=contrast, beta=brightness)
        modified_img = Image.fromarray(modified_array)
        st.image(modified_img, caption="Image after Brightness and Opacity ", use_container_width=True)
        st.download_button(
            label="⬇️ Download the image",
            data=modified_img.tobytes(),
            file_name="modified_image.png",
            mime="image/png"
        )


    # زر العودة
    if st.button("⬅️ Back", key="lesson3_back"):
        st.session_state.page = "home"

# ---------- الدرس الرابع ----------
def lesson4_page():
    main_img = Image.open("PixelWise/Images/L4.png")
    st.image(main_img, use_container_width=True)

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"], key="lesson4_uploader")
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img_array = np.array(img)

        # عرض الصورة الأصلية
        st.image(img, caption="Original image", use_container_width=True)

        # اختيار نوع الفلتر
        filter_type = st.selectbox("Select filter type", ["Gaussian Blur", "Sobel X", "Sobel Y", "Laplacian"])
        if filter_type == "Gaussian Blur":
            filtered_array = cv2.GaussianBlur(img_array, (5,5), 0)
        elif filter_type == "Sobel X":
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            filtered_array = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
            filtered_array = cv2.convertScaleAbs(filtered_array)
            filtered_array = cv2.cvtColor(filtered_array, cv2.COLOR_GRAY2RGB)
        elif filter_type == "Sobel Y":
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            filtered_array = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
            filtered_array = cv2.convertScaleAbs(filtered_array)
            filtered_array = cv2.cvtColor(filtered_array, cv2.COLOR_GRAY2RGB)
        else:  # Laplacian
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            filtered_array = cv2.Laplacian(gray, cv2.CV_64F)
            filtered_array = cv2.convertScaleAbs(filtered_array)
            filtered_array = cv2.cvtColor(filtered_array, cv2.COLOR_GRAY2RGB)

        filtered_img = Image.fromarray(filtered_array)
        st.image(filtered_img, caption=f"Image after applying  {filter_type}", use_container_width=True)

        # زر تنزيل
        st.download_button(
            label=f"⬇️ Download image after {filter_type}",
            data=filtered_img.tobytes(),
            file_name=f"filtered_image_{filter_type.replace(' ','_')}.png",
            mime="image/png"
        )

    # زر العودة
    if st.button("⬅️ Back", key="lesson4_back"):
        st.session_state.page = "home"
# ---------- الدرس الخامس ----------
def lesson5_page():
    main_img = Image.open("PixelWise/Images/L5.png")
    st.image(main_img, use_container_width=True)


    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"], key="lesson5_uploader")
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img_array = np.array(img)

        # عرض الصورة الأصلية
        st.image(img, caption="Original image",  use_container_width=True)

        # اختيار طريقة إزالة الضوضاء
        noise_filter = st.selectbox("Select noise removal method", ["Gaussian Blur", "Median Blur"])
        if noise_filter == "Gaussian Blur":
            denoised_array = cv2.GaussianBlur(img_array, (5,5), 0)
        else:  # Median Blur
            denoised_array = cv2.medianBlur(img_array, 5)

        denoised_img = Image.fromarray(denoised_array)
        st.image(denoised_img, caption=f"Image after applying {noise_filter}",  use_container_width=True)

        # زر تنزيل
        st.download_button(
            label=f"⬇️ Download image after {noise_filter}",
            data=denoised_img.tobytes(),
            file_name=f"denoised_image_{noise_filter.replace(' ','_')}.png",
            mime="image/png"
        )

    # زر العودة
    if st.button("⬅️ Back", key="lesson5_back"):
        st.session_state.page = "home"

# ---------- الدرس السادس ----------
def lesson6_page():
    main_img = Image.open("PixelWise/Images/L6.png")
    st.image(main_img , use_container_width=True)

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"], key="lesson6_uploader")
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        if img.mode != "L":
            img = img.convert("L")  # تحويل الصورة إلى رمادية
        img_array = np.array(img)

        # عرض الصورة الأصلية
        st.image(img, caption="Original image", use_container_width=True)

        # اختيار طريقة كشف الحواف
        edge_method = st.selectbox("Select edge detection method", ["Canny", "Sobel"])
        if edge_method == "Canny":
            edges_array = cv2.Canny(img_array, 100, 200)
        else:  # Sobel
            sobelx = cv2.Sobel(img_array, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(img_array, cv2.CV_64F, 0, 1, ksize=3)
            edges_array = cv2.magnitude(sobelx, sobely)
            edges_array = np.uint8(edges_array)

        edges_img = Image.fromarray(edges_array)
        st.image(edges_img, caption=f"Image after edge detection using {edge_method}", use_container_width=True)

        # زر تنزيل
        st.download_button(
            label=f"⬇️ Download image after edge detection ({edge_method})",
            data=edges_img.tobytes(),
            file_name=f"edges_image_{edge_method}.png",
            mime="image/png"
        )

    # زر العودة
    if st.button("⬅️ Back", key="lesson6_back"):
        st.session_state.page = "home"

# ---------- الدرس السابع ----------
def lesson7_page():
    main_img = Image.open("PixelWise/Images/L7.png")
    st.image(main_img , use_container_width=True)




    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"], key="lesson7_uploader")
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        gray = img.convert("L")
        img_array = np.array(gray)

        # عرض الصورة الأصلية
        st.image(gray, caption="Original image (grayscale)", use_container_width=True)

        # اختيار العملية المورفولوجية
        morph_op = st.selectbox("Select morphological operation", ["Erosion", "Dilation", "Opening", "Closing"])
        kernel_size = st.slider("Kernel size", 1, 10, 3)
        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        if morph_op == "Erosion":
            result_array = cv2.erode(img_array, kernel, iterations=1)
        elif morph_op == "Dilation":
            result_array = cv2.dilate(img_array, kernel, iterations=1)
        elif morph_op == "Opening":
            result_array = cv2.morphologyEx(img_array, cv2.MORPH_OPEN, kernel)
        else:  # Closing
            result_array = cv2.morphologyEx(img_array, cv2.MORPH_CLOSE, kernel)

        result_img = Image.fromarray(result_array)
        st.image(result_img, caption=f"Image after operation {morph_op}", use_container_width=True)

        # زر تنزيل
        st.download_button(
            label=f"⬇️Download image {morph_op}",
            data=result_img.tobytes(),
            file_name=f"morph_{morph_op}.png",
            mime="image/png"
        )

    # زر العودة
    if st.button("⬅️ Back", key="lesson7_back"):
        st.session_state.page = "home"

# ---------- الدرس الثامن ----------
def lesson8_page():
    main_img = Image.open("PixelWise/Images/L8.png")
    st.image(main_img , use_container_width=True)


    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"], key="lesson8_uploader")
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img_array = np.array(img)

        # عرض الصورة الأصلية
        st.image(img, caption="Original image", use_container_width=True)

        # اختيار نوع التحويل
        transform_type = st.selectbox("Select geometric transformation type", ["Rotation angle", "Scaling factor", "Crop"])

        if transform_type == "Rotation angle":
            angle = st.slider("Scaling factor", -180, 180, 0)
            (h, w) = img_array.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            transformed_array = cv2.warpAffine(img_array, M, (w, h))
        elif transform_type == "Zoom in/Zoom out":
            scale = st.slider("Percent of Zoom in/ Zoom out", 0.1, 3.0, 1.0)
            (h, w) = img_array.shape[:2]
            transformed_array = cv2.resize(img_array, (int(w*scale), int(h*scale)))
        else:  # قص
            st.markdown("Specify cropping ratios between 0 and 1")
            x_start = st.slider("Start ratio on width", 0.0, 1.0, 0.0)
            x_end = st.slider("End ratio on width", 0.0, 1.0, 1.0)
            y_start = st.slider("Start ratio on height", 0.0, 1.0, 0.0)
            y_end = st.slider("End ratio on height", 0.0, 1.0, 1.0)
            (h, w) = img_array.shape[:2]
            x1, x2 = int(x_start*w), int(x_end*w)
            y1, y2 = int(y_start*h), int(y_end*h)
            transformed_array = img_array[y1:y2, x1:x2]

        transformed_img = Image.fromarray(transformed_array)
        st.image(transformed_img, caption=f"Image after transformation{transform_type}", use_container_width=True)

        # زر تنزيل
        st.download_button(
            label=f"⬇️ Download image after {transform_type}",
            data=transformed_img.tobytes(),
            file_name=f"transformed_{transform_type}.png",
            mime="image/png"
        )

    # زر العودة
    if st.button("⬅️ Back", key="lesson8_back"):
        st.session_state.page = "home"


# ---------- اختيار الصفحة ----------
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "lesson1":
    lesson1_page()
elif st.session_state.page == "lesson2":
    lesson2_page()
elif st.session_state.page == "lesson3":
    lesson3_page()
elif st.session_state.page == "lesson4":
    lesson4_page()
elif st.session_state.page == "lesson5":
    lesson5_page()
elif st.session_state.page == "lesson6":
    lesson6_page()
elif st.session_state.page == "lesson7":
    lesson7_page()
elif st.session_state.page == "lesson8":
    lesson8_page()


