if status is-interactive
    # Commands to run in interactive sessions can go here
end

set fish_greeting ""

#aliases

#programas

alias ll "lsd -lh --group-dirs=first"
alias la "lsd -a --group-dirs=first"
alias l "lsd --group-dirs=first"
alias lla "lsd -lha --group-dirs=first"
alias ls "lsd --group-dirs=first"
alias cat "bat"
alias r "ranger"
alias v "/bin/nvim"
alias w "wget"
alias gc "git clone"
alias vfm "~/.config/vifm/scripts/vifmrun"
alias mci "sudo make clean install"

#fzf

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

#procesos

alias cl "clear"
alias x "exit"
alias cmx "chmod u+x"
alias cm "chmod"
alias cm7 "chmod +777"
alias .. "cd .."
alias d "pwd"
alias grep "grep --color=auto"
alias egrep "egrep --color=auto"
alias fgrep "fgrep --color=auto"
alias mirror "sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist ; sudo pacman -Syy ; sudo pacman -Syu ; paru"
alias mirrord "sudo reflector --latest 30 --number 10 --sort delay --save /etc/pacman.d/mirrorlist ; sudo pacman -Syy ; sudo pacman -Syu ; paru"
alias mirrors "sudo reflector --latest 30 --number 10 --sort score --save /etc/pacman.d/mirrorlist ; sudo pacman -Syy ; sudo pacman -Syu ; paru"
alias mirrora "sudo reflector --latest 30 --number 10 --sort age --save /etc/pacman.d/mirrorlist ; sudo pacman -Syy ; sudo pacman -Syu ; paru"
alias mirrorx "sudo reflector --age 6 --latest 20  --fastest 20 --threads 5 --sort rate --protocol https --save /etc/pacman.d/mirrorlist ; sudo pacman -Syy ; sudo pacman -Syu ; paru"
alias mirrorxx "sudo reflector --age 6 --latest 20  --fastest 20 --threads 20 --sort rate --protocol https --save /etc/pacman.d/mirrorlist ; sudo pacman -Syy ; sudo pacman -Syu ; paru"
alias mirrorxxx "sudo reflector --verbose --latest 20 --protocol https --sort rate --save /etc/pacman.d/mirrorlist ; sudo pacman -Syy ; sudo pacman -Syu ; paru"

#cd

alias bar "cd ~/.config/polybar"
alias wm "cd ~/.config/bspwm"
alias mangas "cd ~/Mangas"
alias dsp "cd ~/Escritorio"
alias dwd "cd ~/Descargas"
alias vim "cd ~/.config/nvim"
alias sxhkd "cd ~/.config/sxhkd"

#arch

alias pyyu "sudo pacman -Syyu"
alias py "sudo pacman -Syy"
alias p "sudo pacman -S"
alias pr "sudo pacman -R"
alias prs "sudo pacman -Rs"
alias prns "sudo pacman -Rns"

# Prompt

starship init fish | source
