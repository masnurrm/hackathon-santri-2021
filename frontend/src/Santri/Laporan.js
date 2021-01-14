import React from 'react';

export default function Laporan() {
	return (
		<div className="w-4/5 mt-16 mx-auto text-center flex flex-col ">
			<span className="text-4xl">
				Assalamualaikum, <span className="text-main">Nur Muhammad!</span>
			</span>
			<span className=" border-b-2 border-main w-4/5 mx-auto">&nbsp;</span>

			<div className="lapor flex my-6 w-4/5 mx-auto">
				<div className="form w-5/12">
					<span className="text-3xl">Lapor Kesehatan Santri</span>

					<div class="flex my-4">
						<div class="input-icon">
							<i class="mdi mdi-account-outline text-gray-400 text-lg"></i>
						</div>
						<input type="text" class="input-text" placeholder="Nama Lengkap" />
					</div>

					<div class="flex my-4">
						<div class="input-icon">
							<i class="mdi mdi-key-outline text-gray-400 text-lg"></i>
						</div>
						<input type="text" class="input-text" placeholder="Nomor Induk" />
					</div>

					<div class="flex my-4">
						<div class="input-icon">
							<i class="mdi mdi-hospital-box-outline text-gray-400 text-lg"></i>
						</div>
						<input type="text" class="input-text" placeholder="Keluhan" />
					</div>

					<span className="text-xl pt">Pastikan keluhan tidak salah!!</span>
				</div>

				<span className="w-2/12"></span>

				<div className="status w-5/12 ">
					<span className="text-3xl">Status Laporan Santri</span>
					<p className="pt text-left my-2 text-lg">
						Lihat dan cek status laporan yang telah Anda lakukan untuk
						mengetahui status penanganan kesehatan saat ini!
					</p>
				</div>
			</div>

			<div className="flex w-4/5 mx-auto">
				<button className="gradient-button w-5/12">LAPOR</button>
				<span className="w-2/12"></span>
				<button className="gradient-button w-5/12">STATUS LAPORAN</button>
			</div>
		</div>
	);
}
