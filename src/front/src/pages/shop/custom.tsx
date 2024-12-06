// import axios from "axios";
// import { useEffect, useState } from "react";
// import "../../styles/globals.css";
// import Image from "next/image";
// import NavBar from "../../components/navbar";
// import Footer from "../../components/footer";

interface Custom { }

export default function Custom() {
    // const [mods, setmods] = useState<Custom[]>([]);
    // const [loading, setLoading] = useState<boolean>(true);
    // const [error, setError] = useState<string | null>(null);
    //
    // useEffect(() => {
    //     const fetchmods = async () => {
    //         try {
    //             const response = await axios.get(
    //                 "http://localhost:50150/mods/get_custom"
    //             );
    //             const data = response.data;
    //
    //             if (data.status === "Success") {
    //                 setmods(data.data);
    //             } else {
    //                 setError(data.details);
    //             }
    //         } catch (err) {
    //             setError("Failed to fetch custom");
    //         } finally {
    //             setLoading(false);
    //         }
    //     };
    //
    //     fetchmods();
    // }, []);
    //
    // return (
    //     <div className="flex flex-col h-screen overflow-hidden bg-white">
    //         <NavBar />
    //
    //         <main className="flex-grow flex justify-center items-start bg-lavender p-5 text-gray-800 overflow-y-auto">
    //             <div className="info w-full max-w-2xl">
    //                 {loading ? (
    //                     <div className="flex flex-col justify-center items-center min-h-screen w-full">
    //                         <div className="bg-gray-800 rounded-lg p-6">
    //                             <p className="text-white">Loading...</p>
    //                         </div>
    //                     </div>
    //                 ) : error ? (
    //                     <div className="flex flex-col justify-center items-center min-h-screen w-full">
    //                         <div className="bg-gray-800 rounded-lg p-6">
    //                             <p className="text-red-500">{error}</p>
    //                         </div>
    //                     </div>
    //                 ) : mods.length === 0 ? (
    //                     <div className="flex flex-col justify-center items-center min-h-screen w-full">
    //                         <div className="bg-gray-800 rounded-lg p-6">
    //                             <p className="text-white">No custom found</p>
    //                         </div>
    //                     </div>
    //                 ) : (
    //                     <ul>
    //                         {mods.map((mod) => (
    //                             <li key={mod.id} className="mb-4">
    //                                 <a href={mod.link}>
    //                                     <Image
    //                                         src={mod.image_url}
    //                                         width={250}
    //                                         height={250}
    //                                         alt={mod.full_name}
    //                                         className="rounded"
    //                                     />
    //                                 </a>
    //                                 <p>{mod.full_name}</p>
    //                                 <a
    //                                     className="text-white bg-purple-600 hover:bg-purple-700 transition-colors rounded px-2 py-1"
    //                                     href={mod.link}
    //                                 >
    //                                     {mod.band}
    //                                 </a>
    //                             </li>
    //                         ))}
    //                     </ul>
    //                 )}
    //             </div>
    //         </main>
    //
    //         <Footer />
    //     </div>
    // );
}
