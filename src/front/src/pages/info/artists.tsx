import Image from "next/image";
import { useEffect, useState } from "react";
import axios from "axios";
import "../../styles/globals.css";
import NavBar from "../../components/navbar";
import Footer from "../../components/footer";

interface Artist {
    id: string;
    full_name: string;
    band: string;
    link: string;
    image_url: string;
}

export default function Artists() {
    const [artists, setArtists] = useState<Artist[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchArtists = async () => {
            try {
                const response = await axios.get(
                    "http://localhost:50150/artists/get_artists"
                );
                const data = response.data;

                if (data.status === "Success") {
                    setArtists(data.data);
                } else {
                    setError(data.details);
                }
            } catch (err) {
                setError("Failed to fetch artists");
            } finally {
                setLoading(false);
            }
        };

        fetchArtists();
    }, []);

    return (
        <div className="flex flex-col h-screen overflow-hidden bg-white">
            <NavBar />

            <main className="flex-grow flex justify-center items-start bg-lavender p-5 text-gray-800 overflow-y-auto">
                <div className="info w-full max-w-2xl">
                    {loading ? (
                        <div className="flex flex-col justify-center items-center min-h-screen w-full">
                            <div className="bg-gray-800 rounded-lg p-6">
                                <p className="text-white">Loading...</p>
                            </div>
                        </div>
                    ) : error ? (
                        <div className="flex flex-col justify-center items-center min-h-screen w-full">
                            <div className="bg-gray-800 rounded-lg p-6">
                                <p className="text-red-500">{error}</p>
                            </div>
                        </div>
                    ) : artists.length === 0 ? (
                        <div className="flex flex-col justify-center items-center min-h-screen w-full">
                            <div className="bg-gray-800 rounded-lg p-6">
                                <p className="text-white">No artists found</p>
                            </div>
                        </div>
                    ) : (
                        <ul>
                            {artists.map((artist) => (
                                <li key={artist.id} className="mb-4">
                                    <a href={artist.link}>
                                        <Image
                                            src={artist.image_url}
                                            width={250}
                                            height={250}
                                            alt={artist.full_name}
                                            className="rounded"
                                        />
                                    </a>
                                    <p>{artist.full_name}</p>
                                    <a
                                        className="text-white bg-purple-600 hover:bg-purple-700 transition-colors rounded px-2 py-1"
                                        href={artist.link}
                                    >
                                        {artist.band}
                                    </a>
                                </li>
                            ))}
                        </ul>
                    )}
                </div>
            </main>

            <Footer />
        </div>
    );
}
