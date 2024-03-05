# Generate Blogs with AI

This Streamlit-based application allows users to generate blog content using state-of-the-art language models. Users can input a topic, select a word count, and choose a writing style tailored for researchers, data scientists, or common people.

## Getting Started
![Screenshot 2024-03-05 230801](https://github.com/Abrazaque/Blog-Generator-using-Llama2/assets/81006648/3453adbf-42ee-4496-ae88-f23bda08f4b8)

![Screenshot 2024-03-05 230402](https://github.com/Abrazaque/Blog-Generator-using-Llama2/assets/81006648/a44a63c3-62c3-4ecb-881b-e6cb123b45a3)

![3](https://github.com/Abrazaque/Blog-Generator-using-Llama2/assets/81006648/9ff5fe51-a1d9-4e2d-878d-b62d730be9b9)


To use this application, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Install Dependencies**: Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

3. **Download Language Model**: Download the language model (e.g., LLAMA-2 2-7b) from the official source and save it in a directory named `model`. Update the path to the model in the code accordingly.

4. **Run the Application**: Run the Streamlit application by executing the following command:

   ```
   streamlit run app.py
   ```

5. **Generate Blogs**: Input a topic, select the word count and writing style, and click "Generate" to generate blog content.

## Usage

- Input a topic in the text area.
- Select the desired word count using the slider.
- Choose the writing style from the dropdown menu (Researchers, Data Scientist, Common People).
- Click the "Generate" button to generate blog content.
- View the generated blog content and download it as a text file using the provided button.

## Example

![Generate Blogs](screenshot.png)

## Note

- **Model Download**: Ensure to download the language model from the official source and specify the correct path in the code.
- **Model Size**: The size of the language model may affect the application's performance and response time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
