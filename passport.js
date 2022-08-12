const passport = require('passport');
const TwitterStrategy = require('passport-twitter').Strategy;
passport.serializeUser(function(user, done) {
  done(null, user);
});
passport.deserializeUser(function(user, done) {
  done(null, user);
});
passport.use(new TwitterStrategy({
  consumerKey: "rbKnPdpE9dsmGEqK2qJslys2q",
  consumerSecret: "hYSB6Z2TXYrX5IQRJCTo0AxzauQsqVZLONIeGtUVGKdz2zCrRk",
  callbackURL: "http://127.0.0.1:3000/auth/twitter/callback",
  includeEmail:true
},
function(accessToken, refreshToken, profile, done) {
  return done(null, profile);
}
));