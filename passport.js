require('dotenv').config()

const passport = require('passport')
const TwitterStrategy = require('passport-twitter').Strategy
passport.serializeUser(function (user, done) {
  done(null, user)
})
passport.deserializeUser(function (user, done) {
  done(null, user)
})
passport.use(
  new TwitterStrategy(
    {
      consumerKey: process.env.CONSUMER_KEY,
      consumerSecret: process.env.CONSUMER_SECRET,
      callbackURL: 'http://127.0.0.1:3000/auth/twitter/callback',
      includeEmail: true,
    },
    function (accessToken, refreshToken, profile, done) {
      // console.log(profile)
      return done(null, profile)
    }
  )
)
