
1. Pwntools process là gì ?

   Nó giống như dạng một sever(bản lỏ) cho phép chúng ta có thể kết nối và thay đổi theo ý của mình. Nó thuộc trong thư viện pwntools, để tải thì có thể sử dụng lệnh

   ```python

   pip install pwntools

   ```

   Nguồn ở đây mình sử dụng để viết là [pwntools](https://docs.pwntools.com/en/stable/tubes/processes.html).

2. Hướng dẫn sử dụng

   Câu lệnh mở đầu:

   ```python

   class pwnlib.tubes.process.process(argv=None, shell=False, executable=None, cwd=None, env=None, stdin=-1, stdout=<pwnlib.tubes.process.PTY object>, stderr=-2, close_fds=True, preexec_fn=<function process.<lambda>>, raw=True, aslr=None, setuid=None, where='local', display=None, alarm=None, *args, **kwargs)


   ```

   Với các tham số như sau:
   + argv (list): Danh sách các đối số sử dụng trong quá trình tạo process
   + shell (bool): mặc định là False, khi nó là True nó sẽ coi argv như một str thay vì là list
   + cwd (str): Là địa chỉ hoạt động của process, khi không truyên vào thì nó sẽ mặc định là hoạt động tại file hiện tại
   + env (str): Là định dạng ngôn ngữ của giá trị, khi mặc định thì nó sẽ là ngôn ngữ python( Python làm bố)
   + where (str): là địa chỉ chạy của process, chủ yếu được dùng để logging in
   + arlam(int): Dùng để cài đặt thời gian timeout của project

   Ví dụ:
   ```python

   
    from pwn import *
    
    p = process('python')

   ```

   ![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/91966f3f-d8f5-42ab-a396-fd0f41b29de0)

   Câu lệnh tiếp theo là:
   ```python
   name_process.shutdown("sever")
   name_process.proc.stdin.closed
   ```
   Ví dụ:
   ![image](https://github.com/MinhFanBoy/KCSC_tranning/assets/145200520/09bdbf6c-953b-4958-acb8-8e78a3928e85)

   



  
