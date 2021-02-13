import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';
import useGlobal from '../Global';

export default function Laporan() {
	const [globalState, globalActions] = useGlobal();
	const [isLoading, setLoading] = useState(false);
	const [data, setData] = useState(null);

	const history = useHistory();

	const detail = (id) => {
		history.push('/pusat/detail/' + id);
	};

	useEffect(() => {
		if (
			!localStorage.getItem('santri-token') ||
			!globalState.user.is_superuser
		) {
			localStorage.removeItem('santri-token');
			globalActions.removeToken();
			history.push('/pusat');
		}

		setLoading(true);

		axios
			.get(`${process.env.REACT_APP_API_URL}/laporan/`, {
				headers: {
					Authorization: 'Bearer ' + globalState.access,
				},
			})
			.then((res) => {
				setData(res.data);
				setLoading(false);
				console.log(res.data);
			})
			.catch((err) => {
				console.log(err.messages);
				setLoading(false);
			});
	}, []);

	return isLoading ? (
		<p className="text-center text-3xl my-20">Loading...</p>
	) : (
		<div className="flex flex-col text-center	my-12">
			<span className="text-2xl my-2">Dashboard Laporan</span>
			<span className="pt">
				Daftar laporan yang telah dilakukan beserta status penanganan
			</span>

			<table className="table-fixed w-8/12 mx-auto my-6 border border-collapse border-gray-800">
				<thead className="text-main  border border-gray-800">
					<tr>
						<td className="py-2 w-2/12">Waktu</td>
						<td className="py-2 ">Nama</td>
						<td className="py-2 w-2/12">Nomor Induk</td>
						<td className="py-2">Status Penanganan</td>
					</tr>
				</thead>
				<tbody>
					{data &&
						data
							.filter((x) => x.lapor_pusat)
							.map((data, i) => (
								<tr
									className="hover:bg-gray-200 cursor-pointer"
									onClick={(e) => detail(data.id)}
								>
									<td className="py-4 w-2/12">{i + 1}</td>
									<td className="py-4">{data.dilaporkan.nama}</td>
									<td className="py-4">{data.dilaporkan.nomor_induk}</td>
									<td className="py-4">
										<span
											className={
												data.status_laporan == 'Menunggu penanganan'
													? 'text-warn'
													: 'text-main'
											}
										>
											{data.status_laporan}
										</span>
									</td>
								</tr>
							))}
				</tbody>
			</table>
		</div>
	);
}
