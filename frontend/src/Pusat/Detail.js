import React from 'react';

export default function Detail() {
	return (
		<div className="flex flex-col text-center	my-12">
			<span className="text-2xl my-2">Detail Laporan</span>
			<span className="pt">Daftar laporan untuk penindakan lebih lanjut</span>

			<table className="table-fixed w-6/12 mx-auto my-6 text-left detail-table">
				<tr>
					<td>Nama</td>
					<td>Ryo</td>
				</tr>
				<tr>
					<td>Nomor Induk</td>
					<td>Abc</td>
				</tr>
				<tr>
					<td>Keluhan</td>
					<td>Tipes</td>
				</tr>
				<tr>
					<td>Nomor Asrama</td>
					<td>18</td>
				</tr>
				<tr>
					<td>Status Penanganan</td>
					<td>
						<span className="text-warn">Menunggu Penanganan</span>
					</td>
				</tr>
				<tr>
					<td>No. Telp Ortu</td>
					<td>0818101489</td>
				</tr>
				<tr>
					<td>Alamat Asal</td>
					<td>Jl. Kartini no 56</td>
				</tr>
				<tr>
					<td>Nama Pelapor</td>
					<td>Ryo Hilmi</td>
				</tr>
				<tr>
					<td>Waktu Laporan</td>
					<td>14/01/2002 08:59 WIB</td>
				</tr>
			</table>

			<div className="flex justify-between w-1/2 mx-auto">
				<button
					className="gradient-button w-60"
					style={{ alignSelf: 'center' }}
				>
					TELAH DITANGANI
				</button>
				<button
					className="gradient-button w-60"
					style={{ alignSelf: 'center' }}
				>
					LAPOR PUSAT
				</button>
			</div>
		</div>
	);
}
