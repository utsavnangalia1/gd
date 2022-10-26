
const filter = document.getElementsByClassName('search-blog')
const blogdisp = document.getElementById('blog-display')
const clearbtn = document.getElementById('clear')
const hashdisp = document.getElementById('hashtag-display')
const buttons = document.querySelectorAll('#hashtag');


// ${blog.date_uploaded}

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

console.log("hel")

const sendHashtag = (hash) =>{
    $.ajax({
        type: "GET",
        url: 'hashtag/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'hashtag': hash,
        },
        success: (res) => {
            console.log(res)
            const blogs = res.data
            console.log(blogs)
            hashdisp.innerHTML = ``
                blogs.forEach(blog => {
                    h = blog.date_uploaded
                    console.log(h.toLocaleString('en-GB', { timeZone: 'UTC' }))
                    hashdisp.innerHTML += `
                    <div class="contenttb" >
                        <div class="bloghashes">
                            <div><p>#${blog.hashtag}</p></div>&emsp;&emsp;&emsp;
                            <div class="samay"><i class="fa fa-clock-two"></i> ${blog.read_time} mins read</div>
                        </div>
                        <div class="blogdata">
                            <div class="blogcont">
                            <h3 style="font-weight:bold;" onclick="location.href='${blog.link}';">${blog.title}</h3>
                            <p><span style="white-space: pre-line;">${blog.desc}</span></p>
                        </div>  
                        <div class="blogimg" >
                        <img src="/static/img/Blog/${blog.img}">
                        </div>
                    </div>
                    <div class="lwrpnl">
                        <div><span onclick="bookmarkfunc"><i class="fa fa-thin fa-bookmark" style="padding-top:2px;"></i></span></div>
                        <div class="author"> ${blog.date_uploaded}  | by <strong>${blog.author_name}</strong></div>
                    </div>
                </div>  
                    `
                })

        },
        error: (err) => {
            console.log(err)
        }
    })        
}

buttons.forEach(button => {
    button.addEventListener("click", e=>{
        console.log(e.target.value)

        if (clearbtn.classList.contains('not-visible')){
                clearbtn.classList.remove('not-visible')
            }

        blogdisp.classList.add('not-visible')    

        sendHashtag(e.target.value)
    });
  }); 
