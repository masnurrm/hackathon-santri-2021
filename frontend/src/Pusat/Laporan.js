import React from 'react';

export default function Laporan() {
	return (
		<div className="flex flex-col text-center	my-12">
			<span className="text-2xl my-2">Dashboard Laporan</span>
			<span className="pt">
				Daftar laporan yang telah dilakukan beserta status penanganan
			</span>

			<table className="table-fixed w-8/12 mx-auto my-6 border border-collapse border-gray-800">
				<thead className="text-main  border border-gray-800">
					<tr>
						<td className="w-1/12 py-1">No</td>
						<td>Nama</td>
						<td>Nomor Induk</td>
						<td>Status Penanganan</td>
					</tr>
				</thead>
				<tbody>
					<tr className="py-4">
						<td>1</td>
						<td>Lorem ipsum</td>
						<td>Lorem ipsum</td>
						<td>Lorem ipsum</td>
					</tr>
					<tr>
						<td>1</td>
						<td>Lorem ipsum</td>
						<td>Lorem ipsum</td>
						<td>Lorem ipsum</td>
					</tr>
					<tr>
						<td>1</td>
						<td>Lorem ipsum</td>
						<td>Lorem ipsum</td>
						<td>Lorem ipsum</td>
					</tr>
				</tbody>
			</table>
		</div>
	);
}
