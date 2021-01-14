import React from 'react';
import { Link } from 'react-router-dom';

export default function Header() {
	return (
		<div className="flex justify-between gradient text-white w-full p-6 bg-main">
			<span className="text-3xl ml-4">Santri Sehat</span>

			<div className="text-xl mr-4">
				<Link className="link leading-9">Beranda</Link>
				<Link className="link">Tentang</Link>
			</div>
		</div>
	);
}
