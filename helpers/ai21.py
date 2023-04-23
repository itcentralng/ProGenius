import ai21
import os

ai21.api_key = os.environ.get('AI21_API_KEY')

prompts = {
    "about":"""
Write a proposal to Kaduna State Bureau of Statistic for a Document Sharing Software with the following information:

iT Central is a software company in Kaduna, Nigeria. Their mission is to build world class software solutions and foster the growth of the next generation of software developers. They have been in existence for 4 years since 2019 and have worked with organisations such as Julius Berger Plc, Nigerian Air Force, National Institute for Trypanosomiasis Research among others.

The document sharing software will handle storing files from the company reception down to every single department in the organisation. Documents can be traced and their status can be tracked. If a document is done it, it will notify the respective department.

Proposal Components:

About Us
Problem
Solution
Implementation
Cost

Current Section Title: About Us

Current Section Body:
iT Central is a reputable software company based in Kaduna, Nigeria. Our core mission is to provide world-class software solutions to businesses and organisations, while also fostering the growth of the next generation of software developers. With over 4 years of experience in the software development industry, we have gained valuable knowledge and expertise in delivering quality software products to our clients. We have worked with notable organisations such as Julius Berger Plc, Nigerian Air Force, National Institute for Trypanosomiasis Research, among others, and we have a proven track record of success.

At iT Central, we believe in providing innovative and cost-effective solutions to our clients, which is why we are proposing a document sharing software that will meet the needs of your organisation. We understand the importance of efficient document management and we are committed to providing a solution that will simplify the process, improve productivity and ultimately contribute to the growth of your organisation.

Our team of experienced software developers is well equipped to handle this project and deliver a solution that meets your specific requirements. We are confident that our proposed software solution will be an asset to your organisation and contribute to its overall success.

[stopSequence]

Write a proposal to Darulhuda Foundation Schools for a Computer Based Test Software with the following information:

Lexington Technologies a software development company in Toronto, Canada. Their mission is to create software solutions. They have been in existence for 10 years since 2013 and have worked with organisations such as Facebook Inc, Apple Inc and Total Energies  among others.

The computer based test software will allow the school to conduct their tests and examinations online without the need for a physical exam, allow more flexibility. Students can take their tests at home and have their results immediately without having to wait for an examiner to mark.

Proposal Components:

About Us
Problem
Solution
Implementation
Cost

Current Section Title: About Us

Current Section Body:
Lexington Technologies is a renowned software development company based in Toronto, Canada. Our mission is to create innovative and efficient software solutions that meet the needs of our clients. We have been in the software development industry for over 10 years, since 2013, and have worked with notable organizations such as Facebook Inc, Apple Inc, and Total Energies, among others. Our team of experienced software developers is dedicated to delivering quality software products and services that meet the specific needs of our clients.

At Lexington Technologies, we understand the importance of education and the need for an efficient and effective examination process. We are proposing a computer-based test software solution for Darulhuda Foundation Schools that will simplify the examination process and provide more flexibility for both teachers and students. With our software solution, the school can conduct tests and examinations online, eliminating the need for a physical exam location. This allows students to take their tests from home, and their results can be generated immediately without the need for a physical examiner to mark the exams.

Our proposed software solution is tailored to meet the specific needs of Darulhuda Foundation Schools and will provide a secure and reliable platform for online testing. Our team of experienced software developers is well equipped to handle this project and deliver a solution that meets the unique requirements of the school.

At Lexington Technologies, we believe in providing cost-effective and innovative solutions to our clients. We are committed to ensuring that our proposed software solution will be an asset to the school and contribute to the success of the students.

[stopSequence]

Write a proposal to PrimeTech Engineering Limited for a Company Website with the following information:

iHifix is a tech-enabled company in Lagos Nigeria. Their mission is to create software solutions while offering great software training experience. They have been in existence for 2 years since 2020 and have worked with organisations such as KadaHive Limited, InteliWorks Limited and Grill House Restaurant  among others.

The company website will be elegantly designed showcasing the capability of PrimeTech. It will have a modern feel and will display the professionalism of the company. Clients will be able to fill a form to contact PrimeTech. There will be a section showing all the various departments in the company. Another section showing the team with their pictures and background information.

Proposal Components:

About Us
Problem
Solution
Implementation
Cost

Current Section Title: About Us

Current Section Body:
iHifix is a tech-enabled company based in Lagos, Nigeria, with a mission to create innovative software solutions and provide quality software training experiences to individuals and organizations. We have been in existence for two years since 2020 and have worked with notable organizations such as KadaHive Limited, InteliWorks Limited, and Grill House Restaurant, among others. Our team of experienced software developers and trainers is committed to delivering quality software products and services that meet the specific needs of our clients.

We are proposing a company website solution for PrimeTech Engineering Limited that will showcase the capabilities and professionalism of the company. Our website design will have a modern feel and be elegantly designed to provide an exceptional user experience. Clients will be able to fill a form to contact PrimeTech directly, which will increase the efficiency of the company's customer service. The website will have a section that displays all the various departments in the company, which will give visitors an overview of PrimeTech's offerings. Additionally, there will be a section displaying the team with their pictures and background information, which will increase the level of trust and professionalism associated with the company.

Our team of experienced software developers and designers is well equipped to handle this project and deliver a website that meets the unique requirements of PrimeTech Engineering Limited. We will use the latest technology to ensure that the website is secure, responsive, and user-friendly.

At iHifix, we believe in providing cost-effective and innovative solutions to our clients. We are committed to ensuring that our proposed website solution will be an asset to PrimeTech Engineering Limited and contribute to the success of the company.

[stopSequence]

Write a proposal to [client] for [product] with the following information:

[company-description]

[product-description]

Proposal Components:

About Us
Problem
Solution
Implementation
Cost

Current Section Title: About Us

Current Section Body:
    """
}
stopSequence="####"

def propose(company, company_description, client, product, product_description, component, model="j2-grande", maxTokens=500, temperature=0.7):
    response = ai21.Completion.execute(
        model=model,
        prompt=prompts.get(component)
            .replace("[stopSequence]", stopSequence)
            .replace("[client]", client)
            .replace("[product]", product)
            .replace("product-description", product_description)
            .replace("[company]", company)
            .replace("[company-description]", company_description),
        numResults=1,
        maxTokens=maxTokens,
        temperature=temperature,
        topKReturn=0,
        topP=1,
        stopSequences=[stopSequence]
    )
    print(type(response))
    print(response)
    # return response.get("completions").get("data").get("text")