When my cousin asked me to set up a Web site for her company, with the requirement that she be able to easily and frequently add content, I knew that giving her write access to a bunch of HTML files wouldn't cut it. While tried-and-true WordPress could be a solution, it would constrain the frontend design a bit, and more importantly the admin dashboard could be somewhat overwhelming for someone who only wants to make frequent micro-updates of varied content.

So, I thought about it, when I realised: what's the most user-friendly and feature-packed content management system that everyone already knows? The Graph API made it trivial to set up, and after writing the initial code, I can be guaranteed that any further assistance or instruction on my part won't be necessary for anything menial.

If I had more time to work on this, for sure there's a lot I'd work on in the implementation, but what's here now seems to do exactly what it was meant to do reliably; only time will prove the effectiveness of such an approach.

---

Home: Name, Description, and Links on Facebook

Videos: YouTube

Photos: Photos on Facebook + WordPress with [this plugin](http://tintinnabuleur.bcbc.co.uk/2010/02/15/more-fotobook-changes/) and `wordpress.css` stylesheet

Sky's World: Tumblr

Else: `$name`.txt

---

How to set up Facebook CMS:

* Create private (unpublished) Facebook Page

* Create throwaway Facebook account and make it an admin

* Use [Graph API Explorer](http://developers.facebook.com/tools/explorer/) to generate access token with offline_access permission for the throwaway account

* Copy and paste the access token into the `facebook` function in `make.py`

* Configure WordPress and update WordPress domain in `make.py`

Now, any Facebook user with admin rights to the Page will be able to modify the site; just navigate to http://`$domain`/update to push any changes live.

Bonus: if you fork this repo and configure your Web server user's public key with GitHub (`www-data` on my Ubuntu/Apache machine), site backups are automatically thrown into revision control.

---

Finally, [live demo](http://heardmag.com/) (disclaimer: as of 2012-01-01, the content is all placeholder and largely unrelated to the company).
