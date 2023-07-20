import streamlit as st
import gpt_2_simple as gpt2

# Download the GPT-2 model if it hasn't been downloaded yet
gpt2.download_gpt2(model_name='124M')

# Load the pre-trained model
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, model_name='124M')

# Function to generate a response using the GPT-2 model


def generate_response(prompt):
    response = ''
    s1 = 'Sales can be measured in terms of units sold, revenue generated, or the value of transactions. Key performance indicators (KPIs) such as sales volume, average transaction value, and customer acquisition cost are often used to evaluate sales performance and track the effectiveness of sales strategies.'
    s2 = 'The pharmaceutical sector in Russia plays a crucial role in the countrys healthcare system.The trend of sales in Russias pharmaceutical sector shows a positive outlook.'
    s3 = 'Companies such as Pharmstandard, R-Pharm, GEROPHARM, and BIOCAD are among the leading players in the Russian pharmaceutical industry. These companies engage in research and development, production, and distribution of pharmaceutical products, contributing to the growth and development of the sector.'
    s7 = 'Expected revenue to be generated in India is 645198.'

    #print("prompt omg", prompt)
    if 'war' in prompt and 'russia' in prompt:
        return 'War can have a detrimental effect on the pharmaceutical sector in Russia. It can disrupt supply chains, leading to shortages of medicines and raw materials. Damage to infrastructure and manufacturing facilities can hamper production capacity. Healthcare systems may struggle to meet the increased demand for medical services. The diversion of resources and funds towards war efforts may limit investment in healthcare and research. '
    if 'hello' in prompt or 'Hi' in prompt or 'Hello' in prompt:
        return "Hi, I am InsightPulse for DRL. How may I assist you today?"
    # if 'dr' in prompt or 'Dr' in prompt:
    #     return 'Dr. Reddys Laboratories is an Indian multinational pharmaceutical company based in Hyderabad. The company was founded by Kallam Anji Reddy, who previously worked in the mentor institute Indian Drugs and Pharmaceuticals Limited.'
    if 'products' in prompt:
        s10 = 'The total number of products sold is 400. The maximum number of units sold is of product named Stamlo.The least sales is of Clamp.'
        return s10
    if 'company' in prompt or 'companies' in prompt and 'russia' in prompt:
        s3 = 'Companies such as Pharmstandard, R-Pharm, GEROPHARM, and BIOCAD are among the leading players in the Russian pharmaceutical industry. These companies engage in research and development, production, and distribution of pharmaceutical products, contributing to the growth and development of the sector.'
        return s3+s2
    if 'pharma' in prompt and ('russia' or 'Russia') in prompt:
        return s3+s2
    if 'russia' in prompt or 'Russia' in prompt:
        s2 = 'The pharmaceutical sector in Russia plays a crucial role in the countrys healthcare system.The trend of sales in Russias pharmaceutical sector shows a positive outlook.'
        return s1+s2
    if 'revenue' or 'Revenue' in prompt:
        s5 = 'The total expected revenue in Dr. Reddys Laboratories Limited is 4457726.379'
        return s5
    elif 'Total expected quantity to be sold' in prompt or ('quantity' and 'sold') in prompt:
        s6 = 'Expected quantity to be sold across India, Australia, US and England is 4457726.3792 units'
        return s6
    elif 'India' in prompt or 'india' in prompt:
        s7 = 'Expected revenue to be generated in India is 645198.'
        return s1+s7

    elif 'US' in prompt or 'united states' in prompt:
        s8 = 'Expected quantity to be sold across the United states is 1625811 units.'
        return s1+s8

    elif 'sales' in prompt and 'India' in prompt:
        s9 = 'India estimated a total of 76 sales order. This was pursued by the entity named Aurigene Discovery Technologies. The product sold the most is Econorm.'
        return s9+s7

    elif 'sales' in prompt or 'sale' in prompt:
        s1 = 'Sales can be measured in terms of units sold, revenue generated, or the value of transactions. Key performance indicators (KPIs) such as sales volume, average transaction value, and customer acquisition cost are often used to evaluate sales performance and track the effectiveness of sales strategies.'
        return s1
    else:
        response = gpt2.generate(sess, model_name='124M', prefix=prompt,
                                 length=100, temperature=0.7, return_as_list=True)[0]
        return response
    # print(response)
    # return response

# Streamlit web app


def main():
    st.title("InsightPulse")

    # Create an input field for the user to enter a question or prompt
    prompt = st.text_input("Enter a question or prompt")
    print(prompt)
    if st.button("Get Answer"):
        # Generate a response based on the user's input
        response = generate_response(prompt)

        # Display the generated response
        st.text_area("Response", value=response,
                     height=200, max_chars=None, key=None)


# Run the Streamlit web app
if __name__ == "__main__":
    main()
