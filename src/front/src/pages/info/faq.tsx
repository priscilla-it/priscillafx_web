import { useState } from "react";
import "../../styles/globals.css";
import NavBar from "../../components/navbar";
import Footer from "../../components/footer";

interface Faq {
    question: string;
    answer: string;
}

export default function Faq() {
    const [openIndex, setOpenIndex] = useState<number | null>(null);

    const faqs: Faq[] = [
        {
            question: "1. На чем специализируется Priscilla Custom Effects?",
            answer:
                "Priscilla Custom Effects является компанией, которая занимается моддингом, проектированием и производством уникальных печатных плат для музыкального оборудования. В деятельность компании также входит разработка программного обеспечения.",
        },
        {
            question: "2. Какие виды продукции вы изготавливаете?",
            answer:
                "Мы создаем различные типы электронного оборудования, включая гитарные педали, процессоры звуковых эффектов, микрофоны и другие инструменты для музыкантов. Также предоставляем услуги по модификации и ремонту.",
        },
        {
            question: "3. Что такое модификация гитарной педали?",
            answer:
                "Это процесс изменения её электронной схемы для достижения желаемого звука. Это может включать в себя замену компонентов, добавление новых функций и изменению её спецификации.",
        },
        {
            question: "4. Какого качества оборудование вы производите?",
            answer:
                "Все наши продукты изготавливаются вручную с последующим контролем качества.",
        },
        {
            question: "5. Как приобрести вашу продукцию?",
            answer: "Достаточно связаться с нами любым удобным способом.",
        },
        {
            question: "6. Какими службами доставки вы доставляете?",
            answer:
                "CDEK как основная служба, доступны также Почта России и Boxberry.",
        },
        {
            question: "7. Осуществляете ли доставку заграницу?",
            answer: "Нет, пока не планируем.",
        },
    ];

    const toggleFAQ = (index: number) => {
        setOpenIndex(openIndex === index ? null : index);
    };

    return (
        <div className="flex flex-col h-screen overflow-hidden bg-white">
            <NavBar />

            <main className="flex-grow flex justify-center items-start bg-lavender p-5 text-gray-800 overflow-y-auto">
                <div className="info w-full max-w-2xl">
                    {faqs.map((faq, index) => (
                        <div key={index} className="mb-4">
                            <h3
                                className="cursor-pointer font-semibold bg-gray-200 p-3 rounded"
                                onClick={() => toggleFAQ(index)}
                                role="button"
                                tabIndex={0}
                                onKeyDown={(e) => {
                                    if (e.key === "Enter") toggleFAQ(index);
                                }}
                            >
                                {faq.question}
                            </h3>
                            {openIndex === index && (
                                <p className="p-3 border border-gray-300 rounded bg-white">
                                    {faq.answer}
                                </p>
                            )}
                        </div>
                    ))}
                </div>
            </main>

            <Footer />
        </div>
    );
}
