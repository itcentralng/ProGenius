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
    """,
"problem":"""
Write a proposal to Kaduna State Bureau of Statistic for a Document Sharing Software with the following information:

iT Central is a software company in Kaduna, Nigeria. Their mission is to build world class software solutions and foster the growth of the next generation of software developers. They have been in existence for 4 years since 2019 and have worked with organisations such as Julius Berger Plc, Nigerian Air Force, National Institute for Trypanosomiasis Research among others.

The document sharing software will handle storing files from the company reception down to every single department in the organisation. Documents can be traced and their status can be tracked. If a document is done it, it will notify the respective department.

Proposal Components:

About Us
Problem
Solution
Implementation
Cost

Current Section Title: Problem

Current Section Body:
Many organizations face challenges with document management, including issues with document version control, security, and accessibility. Traditional methods of document sharing, such as email and paper-based systems, are not efficient and can lead to delays in the decision-making process, misplaced or lost documents, and potential security breaches.

The Kaduna State Bureau of Statistics is no exception to these challenges. The organization deals with a large volume of documents, ranging from reports and data analysis to official correspondences and administrative documents. These documents are often shared across multiple departments and individuals, leading to a lack of centralized control and coordination.

Furthermore, the current document management system used by the Bureau is outdated, cumbersome, and prone to errors. This often results in delayed response times, lost documents, and duplication of efforts.

To address these challenges, the Kaduna State Bureau of Statistics needs a modern, efficient, and user-friendly document sharing software solution that can improve the organization's document management system.

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

Current Section Title: Problem

Current Section Body:
Darulhuda Foundation Schools faces a major challenge with conducting exams and tests in a timely and efficient manner. Traditional methods of conducting exams, such as pen and paper-based tests, require a large amount of time and resources to administer, grade, and analyze results. This often results in delays in the release of exam results and a lack of flexibility in scheduling exams and tests.

Moreover, in the wake of the COVID-19 pandemic, the need for remote learning and online education has become more critical than ever. The school needs to provide a safe and secure online platform for students to take their exams and tests from home while ensuring the integrity of the exam process.

To address these challenges, Darulhuda Foundation Schools needs a modern, efficient, and secure computer-based test software solution that can streamline the exam process, provide more flexibility in scheduling exams and tests, and ensure the integrity of the exam process while allowing students to take their tests from home.

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

Current Section Title: Problem

Current Section Body:
PrimeTech Engineering Limited faces a major challenge with effectively showcasing their services and capabilities to potential clients. With the increasing trend towards online presence and digital marketing, a company website has become a critical tool for businesses to attract and engage customers.

Moreover, the absence of a company website can leave a negative impression on potential clients, as it can be seen as a lack of professionalism and credibility. This can result in missed opportunities for business growth and revenue.

To address these challenges, PrimeTech Engineering Limited needs a modern, professional, and engaging company website that can effectively showcase the company's services and capabilities, as well as provide potential clients with an easy and convenient way to contact the company.

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

Current Section Title: Problem

Current Section Body:
""",
"solution":"""
Write a proposal to Kaduna State Bureau of Statistic for a Document Sharing Software with the following information:

iT Central is a software company in Kaduna, Nigeria. Their mission is to build world class software solutions and foster the growth of the next generation of software developers. They have been in existence for 4 years since 2019 and have worked with organisations such as Julius Berger Plc, Nigerian Air Force, National Institute for Trypanosomiasis Research among others.

The document sharing software will handle storing files from the company reception down to every single department in the organisation. Documents can be traced and their status can be tracked. If a document is done it, it will notify the respective department.

Proposal Components:

About Us
Problem
Solution
Implementation
Cost

Current Section Title: Solution

Current Section Body:
The proposed solution to the document sharing problem is a cloud-based software that will be designed to handle the storage, tracking and sharing of documents within iT Central and across all its departments. The software will provide an easy-to-use interface that can be accessed from any device with an internet connection.

The software will allow documents to be uploaded and stored in a central repository, with access controls and permissions to ensure that only authorized personnel can view and edit the files. Users will be able to track the status of documents in real-time and receive notifications when documents are ready for review or approval.

The software will also feature a powerful search function that will enable users to quickly find the documents they need. This will be particularly useful for large organizations like iT Central that handle a large volume of documents on a daily basis.

In addition to document storage and tracking, the software will also provide robust collaboration features, including real-time commenting and version control. This will ensure that all stakeholders are kept up-to-date on the latest changes to a document and that feedback can be provided in a timely manner.

Overall, the document sharing software will provide a seamless and efficient solution to the document management needs of iT Central and will greatly enhance productivity and collaboration across all departments.

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

Current Section Title: Solution

Current Section Body:
To solve these problems, we are proposing a computer-based test software that will be designed to allow Darulhuda Foundation Schools to conduct their tests and examinations online. The software will provide a user-friendly interface that can be accessed from any device with an internet connection.

The software will allow the school to create and administer a wide range of tests and examinations, including multiple-choice, fill-in-the-blank, and essay questions. The software will also feature a powerful grading system that will allow teachers to grade exams automatically and provide instant feedback to students.

The computer-based test software will provide students with a more flexible and convenient way to take their exams. Students will be able to take their exams at home, at any time of day, without the need for a physical exam center. This will greatly reduce the logistical challenges associated with conducting traditional paper-based exams.

Besides providing a more flexible and convenient testing experience for students, the software will also help in reducing costs and saving time. With the computer-based test software, there will be no need to print and distribute exam papers, and there will be no need to hire additional staff to oversee exams.

This software will provide a comprehensive and efficient solution to the examination needs of Darulhuda Foundation Schools and will greatly enhance the testing experience for both students and teachers.

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

Current Section Title: Solution

Current Section Body:
Our proposed solution to the problem faced by PrimeTech Engineering Limited is to create a company website that will be elegantly designed and showcase the capabilities of the company. The website will have a modern feel and will display the professionalism of the company to clients and visitors.

The company website will be designed to provide a user-friendly experience for visitors and will be easy to navigate. It will have a responsive design that will allow it to be viewed on any device, including desktops, laptops, tablets, and smartphones.

The website will include a contact form that clients can fill out to get in touch with PrimeTech Engineering Limited. This will make it easy for clients to make inquiries, request quotes, and provide feedback. The website will also include a section showing all the various departments in the company, making it easy for clients to understand the scope of services that PrimeTech Engineering Limited offers.

Additionally, the website will feature a section showcasing the team members of PrimeTech Engineering Limited, along with their pictures and background information. This will help to build trust and credibility with potential clients, as they will be able to see the qualifications and experience of the team members who will be working on their projects.

We believe the company website will provide a comprehensive and efficient solution to the online needs of PrimeTech Engineering Limited and will greatly enhance the company's online presence and credibility.

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

Current Section Title: Solution

Current Section Body:
""",
"implementation":"""
Write a proposal to Kaduna State Bureau of Statistic for a Document Sharing Software with the following information:

iT Central is a software company in Kaduna, Nigeria. Their mission is to build world class software solutions and foster the growth of the next generation of software developers. They have been in existence for 4 years since 2019 and have worked with organisations such as Julius Berger Plc, Nigerian Air Force, National Institute for Trypanosomiasis Research among others.

The document sharing software will handle storing files from the company reception down to every single department in the organisation. Documents can be traced and their status can be tracked. If a document is done it, it will notify the respective department.

Proposal Components:

About Us
Problem
Solution
Implementation
Cost

Current Section Title: Implementation

Current Section Body:
The implementation process for the document sharing software will be carried out in stages, with close collaboration with the Kaduna State Bureau of Statistics to ensure seamless integration with their existing systems and processes. The stages are:

1. Needs Assessment: The iT Central team will work with the Bureau of Statistics to understand their specific needs and requirements for the document sharing software. This will involve assessing the current systems and processes in place, identifying any gaps, and determining the necessary features and functionalities for the software.

2. Design and Development: Based on the needs assessment, the iT Central team will design and develop the document sharing software. This will include creating a user-friendly interface, implementing robust security features, and ensuring that the software is scalable to accommodate future growth and changes in the organization.

3. Testing and Deployment: Once the software has been developed, it will undergo thorough testing to ensure that it meets the Bureau of Statistics' requirements and is functioning optimally. After successful testing, the software will be deployed to the Bureau's systems, and training will be provided to ensure that staff members can use the software effectively.

4. Ongoing Support: The iT Central team will provide ongoing support for the document sharing software, including regular maintenance, updates, and troubleshooting. This will ensure that the software remains reliable and functional over time.

Overall, the implementation of the document sharing software will be a collaborative effort between iT Central and the Bureau of Statistics, with a focus on ensuring that the software meets the Bureau's needs and integrates seamlessly into their existing systems and processes.

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

Current Section Title: Implementation

Current Section Body:
To implement the computer-based test software, Lexington Technologies will work closely with Darulhuda Foundation Schools to ensure a smooth transition from traditional paper-based tests to online computer-based tests. The implementation process will involve the following steps:

1. Consultation: We will schedule a meeting with the school management team to understand their requirements and expectations for the computer-based test software.

2. Customization: We will customize the software to suit the specific needs of Darulhuda Foundation Schools, ensuring that it meets their unique requirements and is user-friendly for both the teachers and students.

3. Training: We will provide training to the school's teachers on how to use the software, including how to set up exams, administer them, and how to interpret the results.

4. Pilot Test: We will conduct a pilot test with a small group of students to ensure that the software is functioning correctly and to address any issues that may arise.

5. Full Rollout: Once the pilot test is successful, we will roll out the software to the entire school. We will provide ongoing support to the school to ensure that the software runs smoothly and any technical issues are addressed promptly.

We understand that transitioning from traditional paper-based tests to online computer-based tests may be a significant change for Darulhuda Foundation Schools, and we are committed to making the implementation process as seamless as possible.

Our team of experienced software developers and project managers will work with the school to ensure that the implementation is carried out efficiently and with minimal disruption to the school's operations.

With our expertise and experience, we are confident that we can successfully implement the computer-based test software at Darulhuda Foundation Schools and deliver the benefits of online testing to the school and its students.

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

Current Section Title: Implementation

Current Section Body:
To ensure a successful implementation of the PrimeTech Engineering Limited company website, iHifix will follow the following steps:

1. Requirement Gathering: Our team will work with PrimeTech Engineering Limited to gather all the necessary requirements for the website. This will involve understanding the goals of the website, the target audience, and the key features to be included.

2. Design: Our team of designers will work to create a modern, elegant design that showcases the professionalism of PrimeTech Engineering Limited. We will use the latest design trends and technologies to create a user-friendly interface that will engage visitors.

3. Development: Our experienced development team will use the latest technologies and coding standards to develop a website that meets the requirements of PrimeTech Engineering Limited. We will ensure that the website is responsive, optimized for speed, and has the necessary functionality required.

4. Testing: Our QA team will thoroughly test the website to ensure that it is functioning correctly and that there are no bugs or errors.

5. Launch: Once the website has been tested and approved by PrimeTech Engineering Limited, we will launch it on the internet.

6. Maintenance and Support: We will provide ongoing maintenance and support for the website, ensuring that it is always up to date and functioning correctly.

Timeline:

We estimate that the implementation of the PrimeTech Engineering Limited company website will take approximately 6-8 weeks from start to finish, depending on the complexity of the project.

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

Current Section Title: Implementation

Current Section Body:
""",
"cost":"""
Write a proposal to Kaduna State Bureau of Statistic for a Document Sharing Software with the following information:

iT Central is a software company in Kaduna, Nigeria. Their mission is to build world class software solutions and foster the growth of the next generation of software developers. They have been in existence for 4 years since 2019 and have worked with organisations such as Julius Berger Plc, Nigerian Air Force, National Institute for Trypanosomiasis Research among others.

The document sharing software will handle storing files from the company reception down to every single department in the organisation. Documents can be traced and their status can be tracked. If a document is done it, it will notify the respective department. Building it will include developing an API to serve the client, a client UI for Users to interact with. The API will cost NGN500,000 while the UI will cost NGN350,000. The cost of hosting and other cloud services will depend on further discussions and clarification of requirements.

Proposal Components:

About Us
Problem
Solution
Implementation
Cost

Current Section Title: Cost

Current Section Body:
The total cost for developing the document sharing software will be NGN850,000, which includes NGN500,000 for the development of the API and NGN350,000 for the development of the client UI. The cost of hosting and other cloud services will depend on further discussions and clarification of requirements.

We understand that cost is an important factor in any software development project, and we assure you that our pricing is competitive and transparent. Our team of experienced developers will work efficiently to ensure that the project is completed within the agreed timeline and budget.

In addition to the initial development cost, there may be ongoing maintenance and support costs, depending on the scope of the project. We will work with you to determine the level of support required and provide a customized service agreement that meets your needs.

Overall, we believe that the benefits of the document sharing software will far outweigh the development and maintenance costs, as it will provide a more efficient and organized way of managing documents within the Kaduna State Bureau of Statistics. We look forward to working with you to bring this project to life.

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

Current Section Title: Cost

Current Section Body:
The cost of implementing the computer based test software will depend on the size of the school and the number of students who will be using the software. We will work with Darulhuda Foundation Schools to create a custom pricing plan that suits their needs and budget. 

We offer a flexible payment plan, which allows the school to pay for the software over a period of time rather than paying the full amount upfront. This payment plan is designed to help the school manage their finances better and make it easier for them to budget for the software.

In addition, we offer free technical support to ensure that the software is running smoothly and that any issues are addressed in a timely manner. This support will be available 24/7, and our team will be on hand to provide assistance whenever it is needed.

We believe that the benefits of using a computer based test software far outweigh the costs, and we are confident that Darulhuda Foundation Schools will see a significant return on their investment. With the ability to conduct tests and exams online, the school can save money on printing and paper costs, and reduce the need for examiners. 

Overall, we are committed to providing affordable and high-quality software solutions to our clients, and we are confident that we can work with Darulhuda Foundation Schools to create a custom pricing plan that meets their needs and budget.

[stopSequence]
Write a proposal to PrimeTech Engineering Limited for a Company Website with the following information:

iHifix is a tech-enabled company in Lagos Nigeria. Their mission is to create software solutions while offering great software training experience. They have been in existence for 2 years since 2020 and have worked with organisations such as KadaHive Limited, InteliWorks Limited and Grill House Restaurant  among others.

The company website will be elegantly designed showcasing the capability of PrimeTech as a reputable Engineering Company. It will have a modern feel and will display the professionalism of the company. Clients will be able to fill a form to contact PrimeTech. There will be a section showing all the various departments in the company. Another section showing the team with their pictures and background information. We will use Wordpress to build this website. We will charge NGN200,000 for building the site and NGN150,000 for annual hosting.

Proposal Components:

About Us
Problem
Solution
Implementation
Cost

Current Section Title: Cost

Current Section Body:
We propose to build the company website for PrimeTech Engineering Limited for a fee of NGN200,000. This fee includes the design, development, and testing of the website, as well as the integration of the necessary functionalities such as contact forms and departmental sections.

In addition, we recommend an annual hosting fee of NGN150,000. This fee covers the cost of website hosting, domain name registration, and website maintenance services. The website will be hosted on a secure server, and regular backups will be performed to ensure data integrity and website availability.

We understand that every client has unique requirements, and as such, we are open to negotiation to tailor our proposal to meet the specific needs of PrimeTech Engineering Limited. Our goal is to provide our clients with cost-effective solutions that meet their business objectives without compromising on quality or functionality.

We look forward to working with PrimeTech Engineering Limited on this project and delivering a world-class website that will enhance their online presence and attract more customers to their business.

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

Current Section Title: Cost

Current Section Body:
""",
"letter":"""
[context]
Write a cover letter based on the above information:
""",
"improve":"""
[context]
Write a better version of the above information:
"""
}
stopSequence="####"

def fewShots(company, company_description, client, offering, description, component, model="j2-grande", maxTokens=500, temperature=0.5):
    response = ai21.Completion.execute(
        model=model,
        prompt=prompts.get(component)
            .replace("[stopSequence]", stopSequence)
            .replace("[client]", client)
            .replace("[product]", offering)
            .replace("product-description", description)
            .replace("[company]", company)
            .replace("[company-description]", company_description),
        numResults=1,
        maxTokens=maxTokens,
        temperature=temperature,
        topKReturn=0,
        topP=1,
        stopSequences=[stopSequence]
    )
    return response.completions[0].data.text

def noShot(component, context, model="j2-jumbo-instruct", maxTokens=1000, temperature=0.5):
    response = ai21.Completion.execute(
        model=model,
        prompt=prompts.get(component)
            .replace("[context]", context),
        numResults=1,
        maxTokens=maxTokens,
        temperature=temperature,
        topKReturn=0,
        topP=1,
        stopSequences=[stopSequence]
    )
    return response.completions[0].data.text

def improve(context, model="j2-jumbo-instruct", maxTokens=1000, temperature=0.5):
    response = ai21.Completion.execute(
        model=model,
        prompt=prompts.get("improve")
            .replace("[context]", context),
        numResults=1,
        maxTokens=maxTokens,
        temperature=temperature,
        topKReturn=0,
        topP=1,
        stopSequences=[stopSequence]
    )
    return response.completions[0].data.text