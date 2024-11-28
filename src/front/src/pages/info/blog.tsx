import axios from "axios";
import { useEffect, useState } from "react";
import "../../styles/globals.css";
import Image from "next/image";
import NavBar from "../../components/navbar";

interface Post {
    created_at: string;
    image_url: string;
    title: string;
    content: string;
    file_url?: string;
}

export default function Blog() {
    const [posts, setPosts] = useState<Post[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchPosts = async () => {
            try {
                const response = await axios.get(
                    "http://localhost:50150/blog/get_posts"
                );
                const data = response.data;

                if (data.status === "Success") {
                    setPosts(data.data);
                } else {
                    setError(data.details);
                }
            } catch (err) {
                setError("Failed to fetch posts");
            } finally {
                setLoading(false);
            }
        };

        fetchPosts();
    }, []);

    const backgroundImage = "/images/backgrounds/blog.jpg";

    return (
        <div className="relative flex flex-col h-screen overflow-hidden bg-black text-white">
            <NavBar />

            <div className="absolute inset-0">
                <Image
                    src={backgroundImage}
                    alt="backgroundImage"
                    fill
                    priority
                    style={{ objectFit: "cover", opacity: 1.0 }}
                />
            </div>

            <main className="flex-grow flex justify-center items-start relative z-10 overflow-y-auto">
                <div className="posts-container w-full max-w-2xl">
                    {loading ? (
                        <p>Loading...</p>
                    ) : error ? (
                        <div className="flex flex-col justify-center items-center min-h-screen w-full">
                            <div className="bg-gray-800 rounded-lg p-6">
                                <p className="text-red-500">{error}</p>
                            </div>
                        </div>
                    ) : posts.length > 0 ? (
                        posts.map((post, index) => (
                            <div
                                key={index}
                                id={`post-${index}`}
                                className="post bg-gray-800 p-5 mb-5 rounded-lg"
                            >
                                <div className="created-at text-gray-400">
                                    {post.created_at}
                                </div>
                                <div>
                                    <a
                                        href={post.image_url}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                    >
                                        <Image
                                            className="image rounded-lg"
                                            src={post.image_url}
                                            alt="image"
                                            width={720}
                                            height={480}
                                        />
                                    </a>
                                </div>
                                <h2 className="title text-2xl mt-2">{post.title}</h2>
                                <div className="content text-gray-300">{post.content}</div>
                                {post.file_url && (
                                    <a
                                        href={post.file_url}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="text-blue-400"
                                    >
                                        Download
                                    </a>
                                )}
                            </div>
                        ))
                    ) : (
                        <div className="flex flex-col justify-center items-center min-h-screen w-full">
                            <div className="bg-gray-800 rounded-lg p-6">
                                <p className="text-white">No posts found</p>
                            </div>
                        </div>
                    )}
                </div>
            </main>

            <footer className="flex justify-center items-center p-3 relative z-10">
                <p>© Priscilla Custom Effects. All rights reserved.</p>
            </footer>
        </div>
    );
}
