import React from 'react';
import { Link, useRouteMatch } from 'react-router-dom';
import useGlobal from '../Global';

export default function Header() {
	let { path, url } = useRouteMatch();
	const [globalState, globalActions] = useGlobal();

	const logout = () => {
		localStorage.removeItem('santri-token');
		globalActions.removeToken();
	};

	return (
		<div className="flex justify-between gradient text-white w-full py-5 px-4 bg-main">
			<span className="text-3xl ml-4">Santri Sehat</span>

			<div className="text-xl mr-4">
				<Link className="link leading-9" to={`${url}`}>
					Beranda
				</Link>
				<Link className="link" to={`${url}/laporan`}>
					Laporan
				</Link>
				<Link className="link" to={`${url}/pengaduan`}>
					Pengaduan
				</Link>
				<Link className="link" to={`${url}/tentang`}>
					Tentang
				</Link>
				{globalState.isLoggedIn && (
					<button href="" className="link" onClick={logout}>
						Keluar
					</button>
				)}
			</div>
		</div>
	);
}
