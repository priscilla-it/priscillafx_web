// import axios from "axios";
// import { useEffect, useState } from "react";
// import "../../styles/globals.css";
// import Image from "next/image";
// import NavBar from "../../components/navbar";
// import Footer from "../../components/footer";
//
// interface SoftwareItem {
//     id: string;
//     name: string;
//     description: string;
//     icon: string;
// }

export default function Software() {
    // const [softwareItems, setSoftwareItems] = useState<SoftwareItem[]>([]);
    // const [loading, setLoading] = useState<boolean>(true);
    // const [error, setError] = useState<string | null>(null);
    //
    // useEffect(() => {
    //     const fetchSoftwareItems = async () => {
    //         try {
    //             const response = await axios.get(
    //                 "http://localhost:50150/software/get_software"
    //             );
    //             const data = response.data;
    //
    //             if (data.status === "Success") {
    //                 setSoftwareItems(data.data);
    //             } else {
    //                 setError(data.details);
    //             }
    //         } catch (err) {
    //             setError("Failed to fetch software");
    //         } finally {
    //             setLoading(false);
    //         }
    //     };
    //
    //     fetchSoftwareItems();
    // }, []);
    //
    // return (
    //     <div className="relative flex flex-col h-screen overflow-hidden bg-white">
    //         <NavBar />
    //
    //         <main className="flex-grow flex justify-center items-start bg-lavender p-5 text-gray-800 overflow-y-auto">
    //             <div className="software-list w-full max-w-2xl">
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
    //                 ) : softwareItems.length > 0 ? (
    //                     <ul>
    //                         {softwareItems.map((software) => (
    //                             <li
    //                                 key={software.id}
    //                                 className="mb-4 p-4 bg-gray-100 rounded-lg"
    //                             >
    //                                 <a
    //                                     href={`/software/${software.id}`}
    //                                     className="flex items-center space-x-4 hover:bg-gray-200 p-2 rounded transition-colors"
    //                                 >
    //                                     <Image
    //                                         src={software.icon}
    //                                         alt={software.name}
    //                                         width={50}
    //                                         height={50}
    //                                         className="rounded"
    //                                     />
    //                                     <div>
    //                                         <h2 className="text-xl">{software.name}</h2>
    //                                         <p className="text-gray-600">{software.description}</p>
    //                                     </div>
    //                                 </a>
    //                             </li>
    //                         ))}
    //                     </ul>
    //                 ) : (
    //                     <div className="flex flex-col justify-center items-center min-h-screen w-full">
    //                         <div className="bg-gray-800 rounded-lg p-6">
    //                             <p className="text-white">No software items found</p>
    //                         </div>
    //                     </div>
    //                 )}
    //             </div>
    //         </main>
    //
    //         <Footer />
    //     </div>
    // );
}
