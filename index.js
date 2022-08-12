const express = require('express')
const app = express()
const cookieSession = require('cookie-session')
const passport = require('passport');
require('./passport')
const isLoggedIn = require('./middleware/auth')
app.use(cookieSession({
  name: 'twitter-auth-session',
  keys: ['key1', 'key2']
}))
app.use(passport.initialize());
app.use(passport.session());
app.get('/',isLoggedIn,(req,res)=>{
  res.send(`Hello ${req.user.displayName}`)
})
app.get('/auth/error', (req, res) => res.send('Unknown Error'))
app.get('/auth/twitter',passport.authenticate('twitter'));
app.get('/auth/twitter/callback',passport.authenticate('twitter', { failureRedirect: '/auth/error' }),
function(req, res) {
  res.redirect('/');
});
app.get('/logout', (req, res) => {
    req.session = null;
    req.logout();
    res.redirect('/');
  })
app.listen(3000,()=>{
  console.log('Server is up and running at the port 3000')
});