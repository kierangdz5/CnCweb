import customtkinter as ctk
from tkinter import Canvas, filedialog
import requests
import json
import webbrowser

API_KEY = "sb5029dec66mht55m78fx8bsw6tm8a"
API_URL = "https://api.snusbase.com/data/search"


class CnCNetwork(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CnC Network Tools")
        self.geometry("1200x800")

        self.main_frame = ctk.CTkFrame(self, fg_color="#0A0A0A",
                                       border_width=4, border_color="#FFD700")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.canvas = Canvas(self.main_frame, bg="#0A0A0A", highlightthickness=0)
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.header = ctk.CTkFrame(self.main_frame, fg_color="#1A0033",
                                   height=80, border_width=3, border_color="#FFD700")
        self.header.pack(fill="x", pady=(0, 10))
        self.header.pack_propagate(False)

        title = ctk.CTkLabel(self.header,
                             text="CnC NETWORK TOOLS",
                             font=ctk.CTkFont("Arial", 32, "bold"),
                             text_color="#FFD700")
        title.pack(pady=20)

        self.content = ctk.CTkFrame(self.main_frame, fg_color="#0F0F1F",
                                    border_width=3, border_color="#FFD700")
        self.content.pack(fill="both", expand=True, padx=20, pady=10)

        self.show_home()

        self.site_button = ctk.CTkButton(
            self.main_frame,
            text="CnC Network",
            width=180,
            height=55,
            corner_radius=0,
            fg_color="#FFD700",
            text_color="#000000",
            hover_color="#B8860B",
            command=self.open_website
        )
        self.site_button.place(relx=0.03, rely=0.92)

    def open_website(self):
        webbrowser.open("https://example.com")

    def show_home(self):
        for widget in self.content.winfo_children():
            widget.destroy()

        label = ctk.CTkLabel(self.content,
                             text="CnC Network Tools",
                             font=ctk.CTkFont("Arial", 40, "bold"),
                             text_color="#FFD700")
        label.pack(pady=80)

        email_btn = ctk.CTkButton(self.content,
                                  text="Email Lookups",
                                  command=self.email_lookup_ui,
                                  width=320,
                                  height=70)
        email_btn.pack(pady=15)

        phone_btn = ctk.CTkButton(self.content,
                                  text="Phone Number Lookups",
                                  command=self.phone_lookup_ui,
                                  width=320,
                                  height=70)
        phone_btn.pack(pady=15)

        ip_btn = ctk.CTkButton(self.content,
                               text="IP Checker",
                               command=self.ip_lookup_ui,
                               width=320,
                               height=70)
        ip_btn.pack(pady=15)

    def email_lookup_ui(self):
        for widget in self.content.winfo_children():
            widget.destroy()

        title = ctk.CTkLabel(self.content,
                             text="Email Lookup",
                             font=ctk.CTkFont("Arial", 30, "bold"),
                             text_color="#FFD700")
        title.pack(pady=40)

        self.email_entry = ctk.CTkEntry(self.content, width=400,
                                        placeholder_text="Enter email...")
        self.email_entry.pack(pady=10)

        self.result_label = ctk.CTkLabel(
            self.content,
            text="",
            text_color="#FFD700",
            wraplength=800,
            justify="left"
        )
        self.result_label.pack(pady=20)

        ctk.CTkButton(self.content,
                      text="Search",
                      command=self.lookup_email,
                      width=300,
                      height=60).pack(pady=10)

        ctk.CTkButton(self.content,
                      text="Download JSON",
                      command=self.download_json,
                      width=300,
                      height=60).pack(pady=10)

        ctk.CTkButton(self.content,
                      text="Back",
                      command=self.show_home,
                      width=300,
                      height=60).pack(pady=20)

    def lookup_email(self):
        email = self.email_entry.get()

        if not email:
            self.result_label.configure(text="Please enter an email")
            return

        headers = {"Auth": API_KEY, "Content-Type": "application/json"}
        payload = {"terms": [email], "types": ["email"]}

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            data = response.json()
            self.last_result = data
            self.result_label.configure(text=json.dumps(data, indent=4))
        else:
            self.result_label.configure(text=f"Error {response.status_code}")

    def download_json(self):
        if not hasattr(self, "last_result"):
            self.result_label.configure(text="No data to download yet.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".json")

        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(self.last_result, f, indent=4)

            self.result_label.configure(text="JSON saved successfully!")

    def phone_lookup_ui(self):
        for widget in self.content.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.content,
                     text="Phone Number Lookups",
                     font=ctk.CTkFont("Arial", 30, "bold"),
                     text_color="#FFD700").pack(pady=40)

        ctk.CTkLabel(self.content,
                     text="Coming soon",
                     font=ctk.CTkFont("Arial", 22),
                     text_color="#BB86FC").pack(pady=20)

        ctk.CTkButton(self.content,
                      text="Back",
                      command=self.show_home,
                      width=300,
                      height=60).pack(pady=20)

    def ip_lookup_ui(self):
        for widget in self.content.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.content,
                     text="IP Checker",
                     font=ctk.CTkFont("Arial", 30, "bold"),
                     text_color="#FFD700").pack(pady=40)

        self.ip_entry = ctk.CTkEntry(self.content, width=400)
        self.ip_entry.pack(pady=10)

        self.result_label = ctk.CTkLabel(
            self.content,
            text="",
            text_color="#FFD700",
            wraplength=800,
            justify="left"
        )
        self.result_label.pack(pady=20)

        ctk.CTkButton(self.content,
                      text="Check IP",
                      command=self.lookup_ip,
                      width=300,
                      height=60).pack(pady=10)

        ctk.CTkButton(self.content,
                      text="Download JSON",
                      command=self.download_json,
                      width=300,
                      height=60).pack(pady=10)

        ctk.CTkButton(self.content,
                      text="Back",
                      command=self.show_home,
                      width=300,
                      height=60).pack(pady=20)

    def lookup_ip(self):
        ip = self.ip_entry.get()
        if not ip:
            self.result_label.configure(text="Please enter an IP")
            return

        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        self.last_result = data
        self.result_label.configure(text=json.dumps(data, indent=4))


if __name__ == "__main__":
    app = CnCNetwork()
    app.mainloop()
