#bin/sh
cp -f isolinux.cfg image/boot/isolinux/
cd image
chmod 444 boot/isolinux/isolinux.cfg
#rm cde/optional/wbar.*
mkisofs -l -J -R -V TCFE -no-emul-boot -boot-load-size 4 -boot-info-table -b boot/isolinux/isolinux.bin -c boot/isolinux/boot.cat -o /home/tc/ezremaster/ezremaster.iso .
