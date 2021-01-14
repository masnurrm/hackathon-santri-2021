import React from 'react';

export default function Login() {
	return (
		<div className="flex w-4/5 mx-auto">
			<img src="/Santri.png" alt="santri" className="w-6/12" />
			<span className="w-1/12"></span>
			<div className="form w-4/12 flex flex-col my-auto">
				<span className="text-gray-600 text-3xl my-2 text-center">
					Pembina Login
				</span>
				<div class="flex my-2">
					<div class="input-icon">
						<i class="mdi mdi-account-outline text-gray-400 text-lg"></i>
					</div>
					<input type="text" class="input-text" placeholder="Nomor Identitas" />
				</div>

				<div class="flex my-2">
					<div class="input-icon">
						<i class="mdi mdi-key-outline text-gray-400 text-lg"></i>
					</div>
					<input type="password" class="input-text" placeholder="Kata Sandi" />
				</div>

				<button className="gradient-button my-2">LOGIN</button>

				<span className="pt text-center">
					Silahkan menuju menu Pengaduan apabila lupa kata sandi
				</span>
			</div>
		</div>
	);
}
